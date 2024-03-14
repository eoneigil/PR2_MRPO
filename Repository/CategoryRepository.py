from Repository import FakeRepository

class CategoryRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.categoryes = []

    def add(self, category):
        self.categoryes.append(category)

    def remove(self, category):
        if self.categoryes:
            for c in self.categoryes:
                if c.name == category.name:
                    self.categoryes.remove(c)

    def get_all(self):
        return self.categoryes

    def get_by_name(self, name):
        if self.categoryes:
            for c in self.categoryes:
                if c.name == name:
                    return c
        return "Категория не найдена"