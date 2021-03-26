"""
main routes file
"""

import asyncio
from concurrent.futures import thread
from typing import Optional
from asyncio.base_events import MAXIMUM_SELECT_TIMEOUT
from fastapi import APIRouter
from utils.kafka_consumer import KafkaConsumer
import concurrent.futures
import multiprocessing
import threading

router = APIRouter(
    prefix="/kafka",
    tags=['Kafka']
)

# kafka_config = {
#     "bootstrap.servers": "pkc-43n10.us-central1.gcp.confluent.cloud:9092",
#     "security.protocol": "SASL_SSL",
#     "sasl.mechanisms": "PLAIN",
#     "sasl.username": "W3LXORK536FBIGCC",
#     "sasl.password": "J6u/jnre7OIetV6Qj6FsyloK/2MUpxWhoQl3Ojye4CgwOxLWD6TXOg17RxS0H0/O",
#     "group.id": "rnr_content_id"
# }

# consumer = None

# consumer = KafkaConsumer(kafka_config, "testing_rnr")
    

#     # loop = asyncio.get_event_loop()
#     # with concurrent.futures.ProcessPoolExecutor() as pool:
#     #     await loop.run_in_executor(pool, consumer.start)

# t = threading.Thread(target=consumer.start(), daemon=True)
# t.start()

# @router.on_event("startup")
# async def startup_event():
#     global consumer
#     consumer = KafkaConsumer(kafka_config, "testing_rnr")
    

#     # loop = asyncio.get_event_loop()
#     # with concurrent.futures.ProcessPoolExecutor() as pool:
#     #     await loop.run_in_executor(pool, consumer.start)

#     p = multiprocessing.Process(target=consumer.start)
#     p.start()
#     p.join()
    

# async def init_consumer():
#     global consumer
#     # while True:
#     await consumer.start()

# @router.on_event("shutdown")
# def shutdown_event():
#     consumer.close()

# @router.get("/")
# def read_root():
#     """
#     Testing this shit
#     """
#     return {"Hello": "World"}

# @router.get("/items/{item_id}")
# def read_item(item_id: int, _q: Optional[str] = None):
#     """
#     Read Item
#     """
#     return {"item_id": item_id, "q": _q}


# @router.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     """
#     Update Item
#     """
#     return {"item_price": item.price, "item_id": item_id}

# @router.get("/{model_name}")
# def get_model(model_name: ModelName):
#     """
#     Get model
#     """
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}
