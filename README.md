# BigData_finalProj
267_final_proj

```
练习时常两年半的project
```

# Set up AWS

Install JAVA 1.8.0_141
```
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u141-b15/336fa29ff2bb4ef291e347e091f7f4a7/jdk-8u141-linux-x64.rpm

sudo yum install -y jdk-8u141-linux-x64.rpm
```

Install Python 3.7
```
sudo yum install python3
sudo yum install python3-pip
sudo pip-3.7 install kafka-python
```

Install Kafka
```
wget https://www-eu.apache.org/dist/kafka/2.2.0/kafka_2.12-2.2.0.tgz
tar -xzf kafka_2.12-2.2.0.tgz 
```

(Optional)Set Kafka limit if machine memory is very small, eg: 1G
```
export KAFKA_HEAP_OPTS="-Xmx250M -Xms250M"
```

Start Kafka
```
cd kafka_2.xx
nohup bin/zookeeper-server-start.sh config/zookeeper.properties > ./zookeeper-logs &
```

Install Spark 2.4
```
wget https://www-eu.apache.org/dist/spark/spark-2.4.2/spark-2.4.2-bin-hadoop2.7.tgz
tar -xzf spark-2.4.2-bin-hadoop2.7.tgz
rm spark-2.4.2-bin-hadoop2.7.tgz 
cd spark-2.4.2-bin-hadoop2.7.tgz 
export SPARK_HOME=$(pwd)
```


Set security groupe, add TCP/Custom port 8080 to inbound rules for your EC2 instance.

# Helpful commands
check port
```
netstat -tulpn | grep 8080
```

check all port
```
sudo lsof -i -P -n
```

start spark monitor in port 8080
```
./sbin/start-master.sh
```

