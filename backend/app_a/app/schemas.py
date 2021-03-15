from typing import Optional
from enum import Enum
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None
    
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"