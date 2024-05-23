from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Repository.SQLRepository import Base
from DBModels.User import UserDB

class EatingDB(Base):
    __tablename__ = 'eatings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))  # Используйте Integer для user_id
    dish = Column(String)

    user = relationship("UserDB")

    def __init__(self, eating_data):
        self.name = eating_data.name
        self.user_id = eating_data.user_id
        self.dish = eating_data.dish

    def to_domain(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id,
            "dish": self.dish
        }
