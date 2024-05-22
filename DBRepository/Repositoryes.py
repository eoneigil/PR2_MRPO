from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from Models.User import User
from Models.Dish import Dish
from Models.Product import Product
from Models.Eating import Eating
from Models.Category import Categoryes

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
            print("IntegrityError: User already exists in the database.")
            if self.session:
                self.session.rollback()

    def remove(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).one_or_none()
        if user:
            try:
                self.session.delete(user)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: User does not exist in the database.")
                self.session.rollback()
        else:
            print(f"User with id {user_id} not found.")

    def remove_by_id(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        if user:
            try:
                self.session.delete(user)
                self.session.commit()
                print(f"User with id {user_id} deleted successfully.")
            except IntegrityError:
                print("IntegrityError: Failed to delete user.")
                self.session.rollback()
        else:
            print(f"User with id {user_id} not found.")

    def get_all(self):
        return self.session.query(User).all()

class DishRepository(BaseRepository):
    def add(self, dish):
        try:
            self.session.add(dish)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: Dish already exists in the database.")
            self.session.rollback()

    def remove(self, dish_id):
        dish = self.session.query(Dish).filter_by(id=dish_id).first()
        if dish:
            try:
                self.session.delete(dish)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Dish does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Dish with id {dish_id} not found.")

    def get_all(self):
        return self.session.query(Dish).all()

class ProductRepository(BaseRepository):
    def add(self, product):
        try:
            self.session.add(product)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: Product already exists in the database.")
            self.session.rollback()

    def remove(self, product_id):
        product = self.session.query(Product).filter_by(id=product_id).first()
        if product:
            try:
                self.session.delete(product)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Product does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Product with id {product_id} not found.")

    def get_all(self):
        return self.session.query(Product).all()

class CategoryRepository(BaseRepository):
    def add(self, category):
        try:
            self.session.add(category)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: Category already exists in the database.")
            self.session.rollback()

    def remove(self, category_id):
        category = self.session.query(Categoryes).filter_by(id=category_id).first()
        if category:
            try:
                self.session.delete(category)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Category does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Category with id {category_id} not found.")

    def get_all(self):
        return self.session.query(Categoryes).all()

class EatingRepository(BaseRepository):
    def add(self, eating):
        try:
            self.session.add(eating)
            self.session.commit()
        except IntegrityError:
            print("IntegrityError: Eating already exists in the database.")
            self.session.rollback()

    def remove(self, eating_id):
        eating = self.session.query(Eating).filter_by(id=eating_id).first()
        if eating:
            try:
                self.session.delete(eating)
                self.session.commit()
            except IntegrityError:
                print("IntegrityError: Eating does not exist in the database.")
                self.session.rollback()
        else:
            print(f"Eating with id {eating_id} not found.")

    def get_all(self):
        return self.session.query(Eating).all()
