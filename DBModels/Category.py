from sqlalchemy import Column, Integer, String
from Repository.SQLRepository import Base

class CategoryDB(Base):
    __tablename__ = 'categoryes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __init__(self, category_data):
        self.name = category_data.name

    def to_domain(self):
        return {
            "id": self.id,
            "name": self.name,
        }