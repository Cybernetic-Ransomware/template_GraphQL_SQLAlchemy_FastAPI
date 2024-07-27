from sqlalchemy.future import select
from sqlalchemy.orm import Session
from app.models import Item
from app.schemas import ItemCreate


def create_item(db: Session, item: ItemCreate):
    db_item = Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def read_items(db: Session):
    query = select(Item)
    result = db.execute(query)
    return result.scalars().all()


def read_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()
