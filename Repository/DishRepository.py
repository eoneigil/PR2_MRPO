from Repository import FakeRepository

class DishRepository(FakeRepository.FakeRepository):
    def __init__(self):
        super().__init__()
        self.dishes = []

    def add(self, dish):  # Изменено с add на add_dish
        self.dishes.append(dish)

    def remove(self, dish_id):  # Изменено с remove на delete_dish
        for dish in self.dishes:
            if dish.id == dish_id:  # Предполагаем, что у блюд есть идентификатор id
                self.dishes.remove(dish)
                break

    def get_all(self):  # Изменено с get_all на get_all_dishes
        return self.dishes

    def get_by_id(self, dish_id):  # Добавлено для соответствия интерфейсу
        for dish in self.dishes:
            if dish.id == dish_id:
                return dish
        return None
