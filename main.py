from Models.Dish import Dish
from Models import User
from Procedures.DishProcedure import DishProcedure
from Procedures.EatingProcedure import EatingProcedure
from Procedures.UserProcedure import UserProcedure
from Procedures.CategoryProcedure import CategoryProcedure
from Repository.XMLRepository import XMLDishRepository, XMLProductRepository
from Repository.XMLRepository import XMLUserRepository
from Services.UserService import UserService
from Repository.XMLRepository import XMLEatingRepository



# Инициализация репозиториев
user_repository = XMLUserRepository("users.xml")
dish_repository = XMLDishRepository("dishes.xml")
eating_repository = XMLEatingRepository("eatings.xml")
product_repository = XMLProductRepository("products.xml")



# Инициализация процедур и сервиса
dish_procedure = DishProcedure(dish_repository, product_repository)
user_procedure = UserProcedure(user_repository)
eating_procedure = EatingProcedure(eating_repository)
user_service = UserService(user_procedure, eating_repository, dish_repository)


# Создание нового блюда с указанием идентификаторов продуктов
new_dish = Dish(1, "Котлета куриная", 480, 30, 5, 10, {1: 3, 2: 45}, category=3)  # Где 1 - id Овсянки
dish_procedure.add_dish_if_meets_nutritional_requirements(new_dish)


# Добавление пользователя
# User3 = User.User(3, 21, 'женский', 45, 165, 'Анна', 'низкая')
# user_procedure.add_user_if_valid(User3)

# Добавление приема пищи для пользователя
# user_service.add_meal_to_user(3, "Овсянка", "Ужин")
user_service.add_meal_to_user(1, "Яйцо с сыром", "Завтрак")

# Вывод всех приемов пищи пользователя
print(user_service.get_all_meals_for_user(1))
