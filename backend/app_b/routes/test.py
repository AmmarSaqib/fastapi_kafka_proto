"""
main routes file
"""


from typing import Optional
from fastapi import APIRouter
from app.schemas import ModelName, Item

router = APIRouter(
    prefix="/test",
    tags=['test']
)

@router.get("/")
def read_root():
    """
    Testing this shit
    """
    return {"Hello": "World"}

@router.get("/items/{item_id}")
def read_item(item_id: int, _q: Optional[str] = None):
    """
    Read Item
    """
    return {"item_id": item_id, "q": _q}


@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """
    Update Item
    """
    return {"item_price": item.price, "item_id": item_id}

@router.get("/{model_name}")
def get_model(model_name: ModelName):
    """
    Get model
    """
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
