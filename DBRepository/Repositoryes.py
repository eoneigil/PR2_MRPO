from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from Models.Dish import Dish
from Models.Product import Product
from Models.Eating import Eating
from Models.Category import Categoryes
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from DBModels.User import User

class BaseRepository(ABC):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def get_all(self):
        pass

class UserRepository(BaseRepository):
    def add(self, user: User):
        try:
            if self.session:
                self.session.add(user)
                self.session.commit()
            else:
                self.users.append(user)
        except IntegrityError:
            print("Пользователь уже есть в БД")
            if self.session:
                self.session.rollback()

    def remove(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).one_or_none()
        if user:
            try:
                self.session.delete(user)
                self.session.commit()
                print(f"Пользователь с айди {user_id} удален.")
            except IntegrityError:
                print("Error")
                self.session.rollback()
        else:
            print(f"Пользователь с айди {user_id} не найден.")

    def get_all(self):
        return self.session.query(User).all()

class DishRepository(BaseRepository):
    def add(self, dish):
        try:
            self.session.add(dish)
            self.session.commit()
        except IntegrityError:
            print("Блюдо уже есть в БД")
            self.session.rollback()

    def remove(self, dish_id):
        dish = self.session.query(Dish).filter_by(id=dish_id).first()
        if dish:
            try:
                self.session.delete(dish)
                self.session.commit()
                print(f"Блюдо с айди {dish_id} удалено")
            except IntegrityError:
                print("Error")
                self.session.rollback()
        else:
            print(f"Блюдо с айди {dish_id} не найдено")

    def get_all(self):
        return self.session.query(Dish).all()

class ProductRepository(BaseRepository):
    def add(self, product):
        try:
            self.session.add(product)
            self.session.commit()
        except IntegrityError:
            print("Продукт уже есть в БД")
            self.session.rollback()

    def remove(self, product_id):
        product = self.session.query(Product).filter_by(id=product_id).first()
        if product:
            try:
                self.session.delete(product)
                self.session.commit()
                print(f"Продукт с айди {product_id} удален")
            except IntegrityError:
                print("Error")
                self.session.rollback()
        else:
            print(f"Продукт с айди {product_id} не найден")

    def get_all(self):
        return self.session.query(Product).all()

class CategoryRepository(BaseRepository):
    def add(self, category):
        try:
            self.session.add(category)
            self.session.commit()
        except IntegrityError:
            print("Категория уже есть в бд")
            self.session.rollback()

    def remove(self, category_id):
        category = self.session.query(Categoryes).filter_by(id=category_id).first()
        if category:
            try:
                self.session.delete(category)
                self.session.commit()
                print(f"Категория с айди {category_id} удалена")
            except IntegrityError:
                print("Error")
                self.session.rollback()
        else:
            print(f"Категория с айди {category_id} не найдена")

    def get_all(self):
        return self.session.query(Categoryes).all()

class EatingRepository(BaseRepository):
    def add(self, eating):
        try:
            self.session.add(eating)
            self.session.commit()
        except IntegrityError:
            print("Прием пищи уже есть в бд")
            self.session.rollback()

    def remove(self, eating_id):
        eating = self.session.query(Eating).filter_by(id=eating_id).first()
        if eating:
            try:
                self.session.delete(eating)
                self.session.commit()
                print(f"Прием пищи с айди {eating_id} удален")
            except IntegrityError:
                print("Error")
                self.session.rollback()
        else:
            print(f"Прием пищи с айди {eating_id} не найден")

    def get_all(self):
        return self.session.query(Eating).all()
