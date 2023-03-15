from kafka import KafkaProducer
import json
import os


BROKER = os.getenv('bnfx_broker')
# bootstrap_servers: 'host[:port]' string (or list of 'host[:port]'
#             strings) that the consumer should contact to bootstrap initial
#             cluster metadata. This does not have to be the full node list.
#             It just needs to have at least one broker that will respond to a
#             Metadata API Request. Default port is 9092. If no servers are
#             specified, will default to localhost:9092.

class Producer:
    topic = ""
    producer = None

    def __init__(self, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(bootstrap_servers=BROKER,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)


    def SendToTopic(self, msg):
        print("sending message...")
        try:
            future = self.producer.send(self.topic,msg)
            self.producer.flush()
            future.get(timeout=60)
            print("message sent successfully...")
            return {'status_code':200, 'error':None}
        except Exception as ex:
            return ex

