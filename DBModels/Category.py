from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categoryes'

    id = Column(Integer, primary_key=True)
    name = Column(String)