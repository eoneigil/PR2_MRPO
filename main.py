import Dish
import Eating
import Category
import Product
import User

from Repository import UserRepository as uR

user1 = User.User(1, 20, 'мужской', 80, 'Иван', 'высокая')
user2 = User.User(2, 21, 'мужской', 65, 'Алишер', 'низкая')
user3 = User.User(3, 21, 'мужской', 72, 'Илья', 'средняя')

product1 = Product.Product('Куриная грудка')
product2 = Product.Product('Гречка')
product3 = Product.Product('Морковь')
product4 = Product.Product('Лук')
product5 = Product.Product('Картофель')
product6 = Product.Product('Рис')

category1 = Category.Categoryes('Постное')
category2 = Category.Categoryes('Без жарки')

eating1 = Eating.Eating(1, user1, 'Завтрак')
eating2 = Eating.Eating(2, user2, 'Обед')
eating3 = Eating.Eating(3, user1, 'Ужин')

dish1 = Dish.Dish(1, 'Запеченная куриная грудка с картофелем', 987, 84, 12, 69, {product1: 200, product5: 150})
dish2 = Dish.Dish(2, 'Гречка с жареной курицей', 1022, 94, 10, 145, {product2: 240, product1: 400})

uRep = uR.UserRepository()

uRep.add(user1)
uRep.add(user2)
uRep.add(user3)

print(uRep.get_all())

uRep.remove(user3)
print(uRep.get_by_name(2))

print(uRep.get_by_name(5))

print(dish1.get_info())
print(dish1.get_info())
