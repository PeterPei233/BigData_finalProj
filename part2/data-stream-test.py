import json

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from time import sleep

data_stream_module = __import__('data-stream')


# 42000 / 3 = 14000
test_input = [
    json.dumps({'Timestamp': '15260000000', 'Symbol': 'BTC-USD', 'LastTradePrice': '10000'}),
    json.dumps({'Timestamp': '15260000001', 'Symbol': 'BTC-USD', 'LastTradePrice': '12000'}),
    json.dumps({'Timestamp': '15260000002', 'Symbol': 'BTC-USD', 'LastTradePrice': '20000'}),
]


class TestKafkaProducer():
    def __init__(self):
        self.target_topic = None
        self.value = None

    def send(self, target_topic, value):
        self.target_topic = target_topic
        self.value = value


def _isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def _make_dstream_helper(sc, ssc, input):
    input_rdds = [sc.parallelize(input, 1)]
    input_stream = ssc.queueStream(input_rdds)
    return input_stream


def test_data_stream(sc, ssc, topic):
    input_stream = _make_dstream_helper(sc, ssc, test_input)

    kafka_producer = TestKafkaProducer()
    data_stream_module.process_stream(input_stream, kafka_producer, topic)

    ssc.start()
    sleep(5)
    ssc.stop()

    assert _isclose(json.loads(kafka_producer.value)['Average'], 14000.0)
    print 'test_data_stream passed!'


if __name__ == '__main__':
    sc = SparkContext('local[2]', 'local-testing')
    ssc = StreamingContext(sc, 1)

    test_data_stream(sc, ssc, 'test_topic')