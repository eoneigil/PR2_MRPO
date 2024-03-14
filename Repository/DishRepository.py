from Repository import FakeRepository

class DishRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.dishes = []

    def add(self, dish):
        self.dishes.append(dish)

    def remove(self, dish):
        if self.dishes:
            for d in self.dishes:
                if d.name == dish.name:
                    self.dishes.remove(d)

    def get_all(self):
        return self.dishes

    def get_by_name(self, name):
        if self.dishes:
            for d in self.dishes:
                if d.name == name:
                    return d
        return "Блюдо не найдено"