from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Repository.UnitOfWork import UnitOfWork
from Repository.SQLRepository import SQLRepository
from DBModels.User import UserDB
from DBModels.Product import ProductDB
from DBModels.Category import CategoryDB
from DBModels.Eating import EatingDB
from ModelsPydantic.UserModel import UserModel
from ModelsPydantic.ProductModel import ProductModel
from ModelsPydantic.CategoryModel import CategoryModel
from ModelsPydantic.EatingModel import EatingModel

app = FastAPI()

# Создание экземпляра репозитория для модели User
user_repo = SQLRepository(UserDB, 'sqlite:///example.db')
product_repo = SQLRepository(ProductDB, 'sqlite:///example.db')
category_repo = SQLRepository(CategoryDB, 'sqlite:///example.db')
eating_repo = SQLRepository(EatingDB, 'sqlite:///example.db')

# Подключение к базе данных
connection_string = 'sqlite:///example.db'
with UnitOfWork(connection_string) as uow:
    session = uow.get_session()


#Эндпоинты для юзеров
@app.post("/users/", response_model=UserModel)
def create_user(user: UserModel):
    db_user = UserDB(user)
    user_repo.add(db_user)
    return db_user

@app.get("/users/", response_model=list[UserModel])
def get_users():
    return user_repo.get_all()

@app.get("/users/{user_id}", response_model=UserModel)
def get_user(user_id: int):
    db_user = user_repo.get_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=UserModel)
def update_user(user_id: int, updated_user: UserModel):
    db_user = user_repo.get_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Обновление данных пользователя
    for field, value in updated_user.dict().items():
        setattr(db_user, field, value)
    user_repo.update(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db_user = user_repo.get_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_repo.delete_by_id(user_id)
    return {"message": "User deleted successfully"}

#Эндпоинты для продуктов
@app.post("/products/", response_model=ProductModel)
def create_product(product: ProductModel):
    db_product = ProductDB(product)
    product_repo.add(db_product)
    return db_product

@app.get("/products/", response_model=list[ProductModel])
def get_products():
    return product_repo.get_all()

@app.get("/products/{product_id}", response_model=ProductModel)
def get_product(product_id: int):
    db_product = product_repo.get_by_id(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{product_id}", response_model=ProductModel)
def update_product(product_id: int, updated_product: ProductModel):
    db_product = product_repo.get_by_id(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    # Обновление данных продукта
    for field, value in updated_product.dict().items():
        setattr(db_product, field, value)
    product_repo.update(db_product)
    return db_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    db_product = product_repo.get_by_id(product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    product_repo.delete_by_id(product_id)
    return {"message": "Product deleted successfully"}

#Эндпоинты для категорий
@app.post("/categoryes/", response_model=CategoryModel)
def create_category(category: CategoryModel):
    db_category = CategoryDB(category)
    category_repo.add(db_category)
    return db_category

@app.get("/categoryes/", response_model=list[CategoryModel])
def get_category():
    return category_repo.get_all()

@app.get("/categoryes/{category_id}", response_model=CategoryModel)
def get_category(category_id: int):
    db_category = category_repo.get_by_id(category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@app.put("/categoryes/{category_id}", response_model=CategoryModel)
def update_category(category_id: int, updated_category: CategoryModel):
    db_category = category_repo.get_by_id(category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    # Обновление данных продукта
    for field, value in updated_category.dict().items():
        setattr(db_category, field, value)
    category_repo.update(db_category)
    return db_category

@app.delete("/categoryes/{category_id}")
def delete_category(category_id: int):
    db_category = category_repo.get_by_id(category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    category_repo.delete_by_id(category_id)
    return {"message": "Category deleted successfully"}

#Эндпоинты для приемов пищи
@app.post("/eatings/", response_model=EatingModel)
def create_eating(eating: EatingModel):
    db_eating = EatingDB(eating)
    eating_repo.add(db_eating)
    return db_eating

@app.get("/eatings/", response_model=list[EatingModel])
def get_eating():
    return eating_repo.get_all()

@app.get("/eatings/{eating_id}", response_model=EatingModel)
def get_eating(eating_id: int):
    db_eating = eating_repo.get_by_id(eating_id)
    if db_eating is None:
        raise HTTPException(status_code=404, detail="Eating not found")
    return db_eating

@app.put("/eatings/{eating_id}", response_model=EatingModel)
def update_eating(eating_id: int, updated_eating: EatingModel):
    db_eating = eating_repo.get_by_id(eating_id)
    if db_eating is None:
        raise HTTPException(status_code=404, detail="Eating not found")
    # Обновление данных продукта
    for field, value in updated_eating.dict().items():
        setattr(db_eating, field, value)
    eating_repo.update(db_eating)
    return db_eating

@app.delete("/eatings/{eating_id}")
def delete_eating(eating_id: int):
    db_eating = eating_repo.get_by_id(eating_id)
    if db_eating is None:
        raise HTTPException(status_code=404, detail="Eating not found")
    eating_repo.delete_by_id(eating_id)
    return {"message": "Eating deleted successfully"}
