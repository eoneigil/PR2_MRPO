from Repository.FakeRepository import FakeRepository
from business_rules import validate_nutritional_values, check_dish_fat, check_dish_carb


class DishProcedure:
    def __init__(self, dish_repository, product_repository):
        self.dish_repository = dish_repository
        self.product_repository = product_repository

    def add_dish_if_meets_nutritional_requirements(self, dish):
        if self.dish_repository.get_by_id(dish.id):
            print(f"Блюдо с id={dish.id} уже существует.")
            return False

        # Проверка, существуют ли все указанные продукты
        for product_id in dish.products.keys():
            if not self.product_repository.get_by_id(product_id):
                print(f"Продукт с id={product_id} не найден.")
                return False

        # Проверка, указана ли категория
        if dish.category is None:
            print("Категория блюда не указана.")
            return False

        self.dish_repository.add(dish)
        print(f"Блюдо '{dish.name}' успешно добавлено.")
        return True

    def recommend_dishes_for_dinner(self):
        all_dishes = self.dish_repository.get_all()
        recommended_dishes = [dish for dish in all_dishes if not check_dish_carb(dish) and not check_dish_fat(dish)]
        return recommended_dishes
