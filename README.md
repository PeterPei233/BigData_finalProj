# BigData_finalProj
267_final_proj

```
练习时常两年半的project
```

# Part I
run zookeeper container
```
docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
```

run kafka container
```
docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=172.17.0.3 -e KAFKA_ADVERTISED_PORT=9092 --name kafka --link zookeeper:zookeeper confluent/kafka
```

run part1 container
```
docker run -d --link kafka:kafka cs502_week10_codelab1
```

run kafka python file
```
docker ps
docker exec -it [container id] sh
python data-consumer.py test kafka:9092
```

# Real Part I

## 1.1
if you use python3, change it to python2. For anacoda, do this:
```
source activate py2
```

## 1.2 Install package

```
pip install requests
pip install schedule
pip install kafka-python
pip freeze > requirements.txt
less requirements.txt
```

### 1.3 set up docker and run the code

``` 
# Start a Zookeeper Container
docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper
confluent/zookeeper
# Start a Kafka Container
docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=localhost -e
KAFKA_ADVERTISED_PORT=9092 --name kafka --link zookeeper:zookeeper
confluent/kafka
Run
 
# Test run
# run data-producer
python data-producer.py BTC-USD test 127.0.0.1:9092
# run data-consumer
# open another terminal, go to your project folder, source virtual environment

python data-consumer.py test 127.0.0.1:9092

```


