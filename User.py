from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    id: int
    age: int
    gender: str
    weight: float
    name: str
    activity: str

    def __eq__(self, other):
        if isinstance(other, User):
            return (self.id == other.id and
                    self.age == other.age and
                    self.gender == other.gender and
                    self.weight == other.weight and
                    self.name == other.name and
                    self.activity == other.activity)
        return False
