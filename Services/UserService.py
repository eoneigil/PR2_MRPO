from Procedures.UserProcedure import UserProcedure
from Repository.EatingRepository import EatingRepository
from Repository.DishRepository import DishRepository  # Import DishRepository
from Models.Eating import Eating
from Repository.XMLRepository import XMLEatingRepository
from Repository.XMLRepository import XMLDishRepository
from Repository.XMLRepository import XMLCategoryRepository

class UserService:
    def __init__(self, user_procedure: UserProcedure, eating_repository: XMLEatingRepository, dish_repository: XMLDishRepository):
        self.user_procedure = user_procedure
        self.eating_repository = eating_repository
        self.dish_repository = dish_repository
        self.eating_counter = 0

    def get_next_eating_id(self):
        self.eating_counter += 1
        return self.eating_counter

    # def add_meal_to_user(self, user_id, dish_name, meal_type):
    #     user = self.user_procedure.get_user_by_id(user_id)
    #     if user:
    #         dish = self.dish_repository.get_by_name(dish_name)
    #         if dish:
    #             next_id = self.get_next_eating_id()
    #             new_eating = Eating(id=next_id, user_id=user.id, name=meal_type, dish=dish.name)
    #             self.eating_repository.add(new_eating)
    #             if user.meals is None:
    #                 user.meals = []
    #             user.meals.append(new_eating)
    #             print(f"Прием пищи '{meal_type}' успешно добавлен для пользователя '{user.name}' с id={user_id}.")
    #         else:
    #             print(f"Блюдо '{dish_name}' не найдено.")
    #     else:
    #         print(f"Пользователь с ID {user_id} не найден.")

    def add_meal_to_user(self, user_id, dish_name, meal_type):
        user = self.user_procedure.get_user_by_id(user_id)
        if not user:
            print(f"Пользователь с ID {user_id} не найден.")
            return

        dish = self.dish_repository.get_by_name(dish_name)
        if not dish:
            print(f"Блюдо '{dish_name}' не найдено.")
            return

        existing_meals = self.eating_repository.get_all()
        user_meals_count = sum(1 for meal in existing_meals if meal.user_id == user.id)

        new_eating_id = user_meals_count + 1
        new_eating = Eating(id=new_eating_id, user_id=user.id, name=meal_type, dish=dish.name)
        self.eating_repository.add(new_eating)
        if user.meals is None:
            user.meals = []
        user.meals.append(new_eating)
        print(f"Прием пищи '{meal_type}' успешно добавлен для пользователя '{user.name}' с id={user_id}.")

    def get_all_meals_for_user(self, user_id):
        user = self.user_procedure.get_user_by_id(user_id)
        if user:
            meals = self.eating_repository.get_all()
            user_meals = [meal for meal in meals if meal.user_id == user_id]
            if user_meals:
                meals_info = []
                for meal in user_meals:
                    dish = self.dish_repository.get_by_name(meal.dish)
                    if dish:
                        meals_info.append(f"{meal.name} - {dish.name}")
                    else:
                        meals_info.append(f"{meal.name} - Неизвестное блюдо")
                meals_str = ", ".join(meals_info)
                return f"Приемы пищи для пользователя {user_id}: {meals_str}"
            else:
                return f"Пользователь {user_id} не имеет приемов пищи."
        else:
            return f"Пользователь с ID {user_id} не найден."





