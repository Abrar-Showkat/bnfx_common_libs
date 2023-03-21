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
    def __init__(topic):
        #self.broker = broker
        producer = None
        broker = "127.0.0.1:9092"
        #self.topic = topic
        #self.producer = KafkaProducer(bootstrap_servers=self.broker,
        producer = KafkaProducer(bootstrap_servers=broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)


    def SendToTopic(topic, msg):
        print("sending message...")
        broker = "127.0.0.1:9092"
        #self.topic = topic
        #self.producer = KafkaProducer(bootstrap_servers=self.broker,
        producer = KafkaProducer(bootstrap_servers=broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries = 3)

        try:
            producer.send(topic,msg)
            producer.flush()
            print("message sent successfully...")
            return {'status_code':200, 'error':None}
        except Exception as ex:
            return (str(ex))

