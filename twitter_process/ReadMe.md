```
    python data-producer.py keyword topic-name port
    e.g. python data-producer.py Avengers tweet 127.0.0.1:9092
```

```
    spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.0.0.jar data-stream.py tweet tweet_analysis 127.0.0.1:9092 5
```

```
    python redis-publisher.py tweet_analysis 127.0.0.1:9092 tweet 127.0.0.1 6379
```

