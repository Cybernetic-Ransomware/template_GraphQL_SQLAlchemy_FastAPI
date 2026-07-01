from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    name: str


class ItemResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)
