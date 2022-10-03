from kafka import KafkaConsumer
from pymongo import MongoClient
import json

#========== to conncet to mongo db ========
db_host = 'mongodb'
db_port = 27017
db_name = 'Tuwaiq'
db_collection = 'Tuwaiq'

client = MongoClient(db_host, db_port) 
db = client[db_name] # conncet to db

#========== for Kafka consumer - to subscribe in the topic ========
topic_name = 'Tuwaiq'
kafka_server = 'kafka:9092'

# get messages from to topic for more info read https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[kafka_server],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    auto_commit_interval_ms=5000,
    fetch_max_bytes=128,
    max_poll_records=100,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')) 
)

# loop to insert all messages in the consumer to mongodb
for message in consumer: 
    tweet = json.loads(json.dumps(message.value)) 
    print (tweet)
    db[db_collection].insert_one(tweet)
