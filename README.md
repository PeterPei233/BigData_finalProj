# BigData_finalProj
267_final_proj

```
练习时常两年半的project
```
![img](https://github.com/PeterPei233/BigData_finalProj/blob/master/cs267_proj.png)

# Real Part I

### 1.1 python2
if you use python3, change it to python2. For anacoda, do this:
```
conda create -n python2 python=2.7 anaconda
source activate python2
```

### 1.2 Install package

```
pip install requests
pip install schedule
pip install kafka-python
pip freeze > requirements.txt
less requirements.txt
```

### 1.3 set up docker and run the code

1. Start a Zookeeper Container
```
docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
```
*** Run in background in ssh example
```
nohup docker run -d -p 2181:2181 -p 2888:2888 -p 3888:3888 --name zookeeper confluent/zookeeper
```
*** If you see demon is not running in AWS, try reboot the docker service manually
```
sudo service docker start
```
2. Start a Kafka Container
```
docker run -d -p 9092:9092 -e KAFKA_ADVERTISED_HOST_NAME=localhost -e KAFKA_ADVERTISED_PORT=9092 --name kafka --link zookeeper:zookeeper confluent/kafka
```
3. run data-producer
```
python data-producer.py twitter test 127.0.0.1:9092
```
4. run data-consumer 
open another terminal, go to your project folder, source virtual environment
```
python data-consumer.py test 127.0.0.1:9092
```

![img](https://github.com/PeterPei233/BigData_finalProj/blob/master/potser.jpg)


