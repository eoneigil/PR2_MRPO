from sqlalchemy import Column, Integer, String
from Repository.SQLRepository import Base

class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    weight = Column(Integer)
    height = Column(Integer)
    activity = Column(String)

    def __init__(self, user_data):
        self.name = user_data.name
        self.age = user_data.age
        self.gender = user_data.gender
        self.weight = user_data.weight
        self.height = user_data.height
        self.activity = user_data.activity

    def to_domain(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "weight": self.weight,
            "height": self.height,
            "activity": self.activity
        }