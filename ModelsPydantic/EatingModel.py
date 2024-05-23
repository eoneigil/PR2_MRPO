from pydantic import BaseModel


class EatingModel(BaseModel):
    id: int
    name: str
    user_id: int
    dish: str