import argparse
import atexit
import json
import logging
import time
from kafka import KafkaProducer
from kafka.errors import KafkaError, KafkaTimeoutError
import sys
import tweepy
from tweepy import TweepError
import configparser
import unicodedata
# unicodedata.normalize('NFKD', title).encode('ascii','ignore')

# reload(sys)
# sys.setdefaultencoding('utf-8')


logger_format = '%(asctime)s - %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('data-producer')
logger.setLevel(logging.DEBUG)



class TweeterStreamListener(tweepy.StreamListener):
    """ A class to read the twitter stream and push it to Kafka"""

    def __init__(self, api, topic, port):
        self.api = api
        self.port = port
        self.topic = topic
        self.i = 0;
        super(tweepy.StreamListener, self).__init__()
#         client = KafkaClient(port)
#         self.producer = KafkaProducer(client, async = True
#                           batch_send_every_n = 1000,
#                           batch_send_every_t = 10)
#         self.producer = KafkaProducer(client, async = True)
        self.producer = KafkaProducer(bootstrap_servers=port)

    def on_status(self, status):
        
        """ This method is called whenever new data arrives from live stream.
        We asynchronously push this data to kafka queue"""

        if hasattr(status, 'retweeted_status'):
            try:
                tweet = status.retweeted_status.extended_tweet["full_text"]
            except:
                tweet = status.retweeted_status.text
        else:
            try:
                tweet = status.extended_tweet["full_text"]
            except AttributeError:
                tweet = status.text


        payload = {'msg': tweet.encode('ascii','ignore'),
                   'coordinates':str(status.coordinates),
                   'Timestamp':str(status.created_at),
                   'location': status.user.location,
                   'place': str(status.place)}
        try:
            logger.debug("Successfully received tweet: {}".format(payload['msg']))
            self.producer.send(topic=self.topic, value=json.dumps(payload))
            logger.debug('Sent twitter info to Kafka.')
        except Exception as e:
            logger.warn('Received info failed due to %s', e)
            return False
        return True

    def on_error(self, status_code):
        logger.warn("Error received in kafka producer, status_code: %d", status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream


def shutdown_hook(producer):
    """
    Helper method to close kafka connections at exit.
    """
    try:
        producer.flush(10)
    except KafkaError as kafka_error:
        logger.warn('Failed to flush pending messages to kafka due to %s', kafka_error.message)
    finally:
        try:
            producer.close(10)
        except Exception as e:
            logger.warn('Failed to clsoe kafka connection due to %s', e.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('track', help='the symbol you want to pull.')
    parser.add_argument('topic_name', help='the kafka topic push to.')
    parser.add_argument('kafka_broker', help='the location of the kafka broker.')

    # Parse arguments.
    args = parser.parse_args()
    track = args.track
    topic_name = args.topic_name
    kafka_broker = args.kafka_broker

    config = configparser.ConfigParser()
    config.read('twitter-app-credentials.txt')
    consumer_key = config['DEFAULT']['consumerKey']
    consumer_secret = config['DEFAULT']['consumerSecret']
    access_key = config['DEFAULT']['accessToken']
    access_secret = config['DEFAULT']['accessTokenSecret']
    
    # Create Auth object
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Instantiate a simple kafka producer.
    producer = KafkaProducer(bootstrap_servers=kafka_broker)

    # Create stream and bind the listener to it
    stream = tweepy.Stream(auth, listener = TweeterStreamListener(api, topic_name, kafka_broker), tweet_mode='extended')

    #Custom Filter rules pull all traffic for those filters in real time.
    #stream.filter(track = ['love', 'hate'], languages = ['en'])
    stream.filter(track = [track], languages = ['en'])

    # Setup proper shutdown hook.
    atexit.register(shutdown_hook, producer)
