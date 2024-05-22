from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True)
class User:
    id: int
    age: int
    gender: str
    weight: float
    height: float
    name: str
    activity: str
    meals: Optional[List['Eating']] = None  # Здесь используется 'Eating' в кавычках

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.id == other.id and
                    self.age == other.age and
                    self.gender == other.gender and
                    self.weight == other.weight and
                    self.height == other.height and
                    self.name == other.name and
                    self.activity == other.activity and
                    self.meals == other.meals)
        return False
