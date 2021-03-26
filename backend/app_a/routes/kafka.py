"""
kafka routes files
"""

import logging
from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.schemas import ModelName, Item
from utils.kafka_producer import KafkaProducer
from confluent_kafka import KafkaException

router = APIRouter(
    prefix="/kafka",
    tags=['Kafka']
)

kafka_config = {
    "bootstrap.servers": "pkc-43n10.us-central1.gcp.confluent.cloud:9092",
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": "W3LXORK536FBIGCC",
    "sasl.password": "J6u/jnre7OIetV6Qj6FsyloK/2MUpxWhoQl3Ojye4CgwOxLWD6TXOg17RxS0H0/O"
}

# "group.id": "rnr_content_id"?

class Item(BaseModel):
    name: str

producer = None

@router.on_event("startup")
async def startup_event():
    global producer
    producer = KafkaProducer( 
        kafka_config)

@router.on_event("shutdown")
def shutdown_event():
    producer.close()

@router.post("/items")
async def create_item(item: Item):
    try:
        result = await producer.produce("testing_rnr", item.name, "name")
        logging.error({ "timestamp": result.timestamp() })
        return { "timestamp": result.timestamp() }
    except KafkaException as ex:
        raise HTTPException(status_code=500, detail=ex.args[0].str())

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
