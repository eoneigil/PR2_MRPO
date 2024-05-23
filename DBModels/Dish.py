from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from DBModels.Dish_Product import dish_product

Base = declarative_base()

class DishDB(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    protein = Column(Integer)
    fat = Column(Integer)
    carb = Column(Integer)
    category = Column(Integer)
    calorifik = Column(Integer)
    products = relationship("Product", secondary=dish_product, back_populates="dishes")