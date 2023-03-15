from kafka import KafkaConsumer, consumer
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
#Subscribe to a list of topic_events, or a topic regex pattern.

class Consumer:
    broker = ""
    topic = ""
    logger = None

    def __init__(self, topic, broker, group_id):
        self.topic = topic
        self.broker = broker
        self.group_id = group_id

    def ReadFromTopic(topic):
        consumer = KafkaConsumer(bootstrap_servers=BROKER, 
            api_version=API_VERSION, 
            consumer_timeout_ms=int(REQUEST_TIMEOUT_MS), 
            enable_auto_commit=False, 
            value_deserializer=lambda m: json.loads(m.decode('ascii')))
        consumer.subscribe(topic)
        return consumer