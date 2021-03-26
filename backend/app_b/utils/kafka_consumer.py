"""
Author: Ammar Saqib
"""

from confluent_kafka import Consumer, KafkaException
import sys
import logging
from pprint import pformat

# @staticmethod
def print_assignment(consumer, partitions):
    """
    """
    logging.error('Assignment:', partitions)

class KafkaConsumer:

    def __init__(self, creds, topic):
        
        if type(topic) != list:
            topic = [topic]
        
        self.__topic = topic
        self.__logger = self.__get_logger()
        self.__consumer = Consumer(creds, logger=self.__logger)

        self.__consumer.subscribe(self.__topic, on_assign=print_assignment)

    def __get_logger(self):
        """
        Setting up logger
        """

        logger = logging.getLogger('consumer')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
        logger.addHandler(handler)

        return logger

    def close(self):
        """
        Closes kafka consumer 
        """

        self.__consumer.close()

    def start(self):
        """
        Initiate Kafka consumer
        """
        # logging.error("it has stgarted")
        
        try:
            while True:
                # logging.error("it has stgarted")
                msg = self.__consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    raise KafkaException(msg.error())
                else:
                    # Proper message
                    sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                    (msg.topic(), msg.partition(), msg.offset(),
                                    str(msg.key())))
                    self.__logger.debug(msg.value())
        except Exception as e:
            logging.error("ashdkf")
        
        finally:
            self.__consumer.close()