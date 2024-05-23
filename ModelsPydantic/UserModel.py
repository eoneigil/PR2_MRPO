from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    weight: int
    height: int
    activity: str