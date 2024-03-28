from Dish import Dish
from User import User
from Product import Product


# Правило проверки калорийности блюда
# def check_calories(dish: Dish, target_calories: float) -> bool:
#     if dish.calorifik <= target_calories:
#         print(f'Блюдо "{dish.name}" подходит по калорийности (Калорийность блюда: {dish.calorifik} ккал)')
#         return True
#     else:
#         print(f'Блюдо "{dish.name}" не подходит по калорийности (Калорийность блюда: {dish.calorifik} ккал)')
#         return False
#
# # Правило проверки исключения продуктов
# def check_product_in_dish(dish: Dish, product: Product) -> bool:
#     if product in dish.products.keys():
#         print(f'Продукт "{product.name}" есть в блюде "{dish.name}"')
#         return True
#     else:
#         print(f'Продукта "{product.name}" нет в блюде "{dish.name}"')
#         return False
#
# #
# # # Правило проверки активности пользователя
# # def check_user_activity(user: User, dish: Dish) -> bool:
# #     if user.activity == 'высокая' and dish.calorifik > 800:
# #         print('Исходя из вашей активности вам подходят блюда калорийностью до 800')
# #         return False
# #     elif user.activity == 'низкая' and dish.calorifik > 600:
# #         print('Исходя из вашей активности вам подходят блюда калорийностью до 600')
# #         return False
# #     return True

def check_dish_carb(dish: Dish) -> bool:
    if dish.carb > 50:
        print(f'Блюдо "{dish.name}"  не подходит для ужина (высокое содержание углеводов)')
        return True
    else:
        return False

def check_dish_fat(dish: Dish) -> bool:
    if dish.fat > 20:
        print(f'Блюдо "{dish.name}" не подходит для ужина (высокое содержание жиров)')
        return True
    else:
        return False

def validate_nutritional_values(dish: Dish) -> bool:
    if dish.calorifik < 0 or dish.protein < 0 or dish.fat < 0 or dish.carb < 0:
        print(f'Ошибка: У блюда "{dish.name}" отрицательные значения калорийности или БЖУ.')
        return False
    return True

def validate_user_height(height: float) -> bool:
    if 40 <= height <= 240:
        return True
    else:
        print('Ошибка: Рост пользователя должен быть в диапазоне от 40 до 240 см.')
        return False
