from fastapi import APIRouter, HTTPException
from app.models import Item

router = APIRouter()

# in-memory database
items_db = []

@router.get("/items")
def get_items():
    return items_db

@router.post("/items")
def create_item(item: Item):
    items_db.append(item)
    return {"message": "Item created", "item": item}

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items_db
    for i, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(i)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")