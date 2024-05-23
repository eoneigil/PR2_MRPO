from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Repository.SQLRepository import Base


class ProductDB(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    # Если в вашей базе данных есть связь многие-ко-многим с другой таблицей,
    # вы можете добавить здесь соответствующие отношения.
    # Пример:
    # dishes = relationship("Dish", secondary=dish_product, back_populates="products")

    def __init__(self, product_data):
        self.name = product_data.name

    def to_domain(self):
        return {
            "id": self.id,
            "name": self.name,
            # Если у вас есть дополнительные поля или связи, их также можно включить здесь
        }
