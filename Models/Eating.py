from dataclasses import dataclass
from Models.User import User

@dataclass(frozen=True)
class Eating:
    id: int
    user_id: int
    name: str
    dish: str
