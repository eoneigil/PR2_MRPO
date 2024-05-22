from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey

Base = declarative_base()

class Eating(Base):
    __tablename__ = 'eatings'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(String)
    dish = Column(String)