from kafka import KafkaConsumer, consumer
from kafka.structs import TopicPartition
import json
import os


BROKER = os.getenv('bnfx_broker')
# bootstrap_servers: 'host[:port]' string (or list of 'host[:port]'
#             strings) that the consumer should contact to bootstrap initial
#             cluster metadata. This does not have to be the full node list.
#             It just needs to have at least one broker that will respond to a
#             Metadata API Request. Default port is 9092. If no servers are
#             specified, will default to localhost:9092.
API_VERSION = os.getenv('bnfx_api_version')
# api_version (tuple): Specify which Kafka API version to use. If set to
#             None, the client will attempt to infer the broker version by probing
#             various APIs. Different versions enable different functionality.
REQUEST_TIMEOUT_MS = os.getenv('bnfx_request_timeout_ms')
# request_timeout_ms (int): Client request timeout in milliseconds.
#             Default: 305000.
# TOPIC_EVENTS = os.getenv('topic_events')
# Subscribe to a list of topic_events, or a topic regex pattern.


class Consumer:
    broker = ""
    topic = ""
    logger = None

    def __init__(topic, group_id):
        consumer = None
        broker = "127.0.0.1:9092"
        #self.topic = topic
        #self.producer = KafkaProducer(bootstrap_servers=self.broker,
        consumer = KafkaConsumer(bootstrap_servers=broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)

    def ReadFromTopic(topic):
        bootstrap_servers = '127.0.0.1:9092'
        try:
            consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest')
            partitions = consumer.partitions_for_topic(topic)
            finalMsg = ""
            for p in partitions:
                topic_partition = TopicPartition(topic, p)
                # Seek offset 0
                consumer.seek(partition=topic_partition, offset=0)
                for msg in consumer:
                    print(msg.value.decode("utf-8"))
                    finalMsg = finalMsg + "" + msg.value.decode("utf-8")
            return {finalMsg}
        except Exception as ex:
            return (str(ex))
    
