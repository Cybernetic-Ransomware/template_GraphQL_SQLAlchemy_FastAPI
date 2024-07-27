from fastapi import Depends

from sqlalchemy.orm import Session
from app.db.database import get_db


async def get_context(db: Session = Depends(get_db)):
    return {
        "db": db
    }
