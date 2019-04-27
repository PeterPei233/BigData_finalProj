# BigData_finalProj
267_final_proj

```
练习时常两年半的project
```
# AWS profile
- [x] t2micro basic setup  | ec2-18-206-200-87.compute-1.amazonaws.com
- [x] t2medium basic setup | ec2-3-88-146-174.compute-1.amazonaws.com
- [x] t2xlarge basic setup | ec2-52-23-153-45.compute-1.amazonaws.com
- [ ] m3xlarge basic setup (cluster) | ec2-52-3-254-27.compute-1.amazonaws.com
- [ ] run kafka pipeline
- [ ] run spark pipeline
- [ ] benchmark kafka
- [ ] benchmark spark

# SSH AWS
Use the cs267.pom tocken in the repo
access ec2
```
ssh -i cs267.pem ec2-user@ec2-xx-xxx-xxx-xx.compute-1.amazonaws.com
```
access cluster
```
ssh -i cs267.pem hadoop@ec2-52-3-254-27.compute-1.amazonaws.com
```
# Set up AWS

Install JAVA 1.8.0_141
```
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u141-b15/336fa29ff2bb4ef291e347e091f7f4a7/jdk-8u141-linux-x64.rpm

sudo yum install -y jdk-8u141-linux-x64.rpm
```

Install Python 3.7 and pip-python2&3
```
sudo yum install python3
sudo yum install python3-pip
sudo yum install python2-pip
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
cd spark-2.4.2-bin-hadoop2.7/
export SPARK_HOME=$(pwd)
```

Set security groupe, add TCP/Custom port 8080 to inbound rules for your EC2 instance.

Others (git, dockers)
```
sudo su
sudo yum update -y
yum install git
yum install -y docker

```
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

