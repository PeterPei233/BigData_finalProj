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
