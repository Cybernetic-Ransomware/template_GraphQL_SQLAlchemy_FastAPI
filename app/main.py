from fastapi import FastAPI, Depends, HTTPException
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.orm import Session


from app.connector import create_item, read_items, read_item
from app.db.database import engine, Base, get_db
from app.graphql.context import get_context
from app.graphql.schema import schema
from app.logger.conf_log import setup_logger, get_logger
from app.schemas import ItemCreate, ItemResponse


setup_logger()
logger = get_logger(__name__)

Base.metadata.create_all(bind=engine)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)


app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"Hello": "World"}


@app.post("/items/", response_model=ItemResponse)
def create_item_rest(item: ItemCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating item: {item}")
    db_item = create_item(db, item)
    return db_item


@app.get("/items/", response_model=list[ItemResponse])
def read_items_rest(db: Session = Depends(get_db)):
    logger.info("Reading all items")
    items = read_items(db)
    return items


@app.get("/item/{item_id}", response_model=ItemResponse)
def read_item_rest(item_id: int, db: Session = Depends(get_db)):
    logger.info(f"Reading item with ID: {item_id}")

    db_item = read_item(db, item_id)
    if db_item is None:
        logger.error(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item with ID {item_id} not found")

    return db_item
