from dataclasses import dataclass
from User import User  # Импортируем класс User, так как класс Eating использует его

@dataclass(frozen=True)
class Eating:
    id: int
    user: User
    name: str
    dish: str