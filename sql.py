from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
import xml.etree.ElementTree as ET
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from DBRepository.Repositoryes import UserRepository, DishRepository, ProductRepository, CategoryRepository, EatingRepository

# Создаем движок и сессию
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()


# Создаем базовую модель
Base = declarative_base()

# Описание таблицы для связи блюд и продуктов
dish_product = Table('dish_product', Base.metadata,
    Column('dish_id', Integer, ForeignKey('dishes.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id'), primary_key=True),
    Column('amount', Integer)
)

# Определение моделей
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    weight = Column(Integer)
    height = Column(Integer)
    activity = Column(String)

class Category(Base):
    __tablename__ = 'categoryes'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Eating(Base):
    __tablename__ = 'eatings'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(String)
    dish = Column(String)

class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    protein = Column(Integer)
    fat = Column(Integer)
    carb = Column(Integer)
    category = Column(Integer)
    calorifik = Column(Integer)
    products = relationship("Product", secondary=dish_product, back_populates="dishes")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    dishes = relationship("Dish", secondary=dish_product, back_populates="products")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Инициализация репозиториев
user_repository = UserRepository(session)
product_repository = ProductRepository(session)
dish_repository = DishRepository(session)
caregory_repository = CategoryRepository(session)
eating_repository = EatingRepository(session)

def read_users_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    users = []
    for user_elem in root.findall('.//user'):
        user_data = {
            'id': int(user_elem.find('id').text),
            'age': int(user_elem.find('age').text),
            'gender': user_elem.find('gender').text,
            'weight': int(user_elem.find('weight').text),
            'height': int(user_elem.find('height').text),
            'name': user_elem.find('name').text,
            'activity': user_elem.find('activity').text,
        }
        users.append(user_data)
    return users

def read_categoryes_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    categoryes = []
    for category_elem in root.findall('.//category'):
        category_data = {
            'id': int(category_elem.find('id').text),
            'name': category_elem.find('name').text,
        }
        categoryes.append(category_data)
    return categoryes

def read_eatings_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    eatings = []
    for eating_elem in root.findall('.//eating'):
        eating_data = {
            'id': int(eating_elem.find('id').text),
            'name': eating_elem.find('name').text,
            'user_id': eating_elem.find('user_id').text,
            'dish': eating_elem.find('dish').text,
        }
        eatings.append(eating_data)
    return eatings

def read_products_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    products = []
    for product_elem in root.findall('.//product'):
        product_data = {
            'id': int(product_elem.find('id').text),
            'name': str(product_elem.find('name').text),
        }
        products.append(product_data)
    return products

def read_dishes_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    dishes = []
    for dish_elem in root.findall('.//dish'):
        dish_data = {
            'id': int(dish_elem.find('id').text),
            'name': dish_elem.find('name').text,
            'protein': int(dish_elem.find('protein').text),
            'calorifik': int(dish_elem.find('calorifik').text),
            'fat': int(dish_elem.find('fat').text),
            'carb': int(dish_elem.find('carb').text),
            'category': int(dish_elem.find('category').text),
        }
        products = []
        products_elem = dish_elem.find('products')
        if products_elem is not None:
            for product_elem in products_elem.findall('.//product'):
                product_id = int(product_elem.find('product_id').text)
                amount = int(product_elem.find('amount').text)
                products.append({'product_id': product_id, 'amount': amount})
        dish_data['products'] = products
        dishes.append(dish_data)
    return dishes

def delete_user_by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        try:
            session.delete(user)
            session.commit()
            print(f"Пользователь с айди {user_id} удален успешно.")
        except IntegrityError:
            print("Ошибка удаления пользователя")
            session.rollback()
    else:
        print(f"Пользователь с айди {user_id} не найден.")


if __name__ == "__main__":
    users_data = read_users_from_xml('users.xml')
    products_data = read_products_from_xml('products.xml')
    dishes_data = read_dishes_from_xml('dishes.xml')
    categoryes_data = read_categoryes_from_xml('categories.xml')
    eatings_data = read_eatings_from_xml('eatings.xml')

    session.query(Product).delete()
    session.query(Dish).delete()

    # Запись пользователей в базу данных
    for user_data in users_data:
        user_repository.add(User(**user_data))

    # Запись категорий в базу данных
    for category_data in categoryes_data:
        caregory_repository.add(Category(**category_data))

    # Запись приемов пищи в базу данных
    for eating_data in eatings_data:
        eating_repository.add(Eating(**eating_data))

    # Запись продуктов в базу данных
    for product_data in products_data:
        product_repository.add(Product(**product_data))

    # Запись блюд в базу данных
    for dish_data in dishes_data:
        products = dish_data.pop('products')
        dish = Dish(**dish_data)
        try:
            dish_repository.add(dish)
        except IntegrityError:
            print(f"IntegrityError: Dish with id {dish.id} already exists in the database.")
            continue

        # Теперь заполняем таблицу dish_product напрямую
        for product_info in products:
            try:
                stmt = dish_product.insert().values(
                    dish_id=dish.id,
                    product_id=product_info['product_id'],
                    amount=product_info['amount']
                )
                session.execute(stmt)
            except IntegrityError:
                print(f"IntegrityError: DishProduct with dish_id {dish.id} and product_id {product_info['product_id']} already exists in the database.")

    user_repository.remove_by_id(1)

    session.commit()
