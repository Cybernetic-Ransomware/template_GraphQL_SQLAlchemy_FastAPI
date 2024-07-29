import asyncio
import strawberry

from typing import AsyncGenerator

from sqlalchemy.orm import Session
from strawberry.types import Info

from app.connector import create_item, read_items, read_item
from app.schemas import ItemCreate
from app.models import Item


@strawberry.type
class ItemType:
    id: int
    name: str


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def items(self, info: Info) -> list[ItemType]:
        db: Session = info.context["db"]
        db_items = read_items(db)
        return [ItemType(id=item.id, name=item.name) for item in db_items]

    @strawberry.field
    def item(self, info: Info, item_id: int) -> ItemType:
        db: Session = info.context["db"]
        db_item = read_item(db, item_id)
        if db_item is None:
            raise ValueError("Item not found")
        return ItemType(id=db_item.id, name=db_item.name)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, info: Info, name: str) -> ItemType:
        db: Session = info.context["db"]
        item_create = ItemCreate(name=name)
        db_item = create_item(db, item_create)
        return ItemType(id=db_item.id, name=db_item.name)


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)
