"""
Author: Ammar Saqib

Main file to trigger the Uvicorn server
"""

import os
import uvicorn
import logging
from app.main import app

from utils.kafka_consumer import KafkaConsumer
import threading

kafka_config = {
    "bootstrap.servers": "pkc-43n10.us-central1.gcp.confluent.cloud:9092",
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": "W3LXORK536FBIGCC",
    "sasl.password": "J6u/jnre7OIetV6Qj6FsyloK/2MUpxWhoQl3Ojye4CgwOxLWD6TXOg17RxS0H0/O",
    "group.id": "rnr_content_id"
}

consumer = None

consumer = KafkaConsumer(kafka_config, "testing_rnr")
    

    # loop = asyncio.get_event_loop()
    # with concurrent.futures.ProcessPoolExecutor() as pool:
    #     await loop.run_in_executor(pool, consumer.start)




if __name__ == "__main__":
    # logging.info(os.environ.get("APP_B_PORT"))
    t = threading.Thread(target=consumer.start, daemon=True)
    t.start()

    # a = threading.Thread(target=uvicorn.run, args=(app,), kwargs={"host":'0.0.0.0', "port":3060}, daemon=True)
    # a.start()
    uvicorn.run(app, host='0.0.0.0', port=3060)
