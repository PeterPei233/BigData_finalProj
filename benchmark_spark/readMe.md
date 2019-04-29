```
cat x* > large.txt

./spark-2.4.0-bin-hadoop2.7/bin/spark-submit --master local[4] wordcount.py large.txt
```
