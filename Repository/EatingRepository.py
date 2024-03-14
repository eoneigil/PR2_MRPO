from Repository import FakeRepository

class EatingRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.eatings = []

    def add(self, eating):
        self.eatings.append(eating)

    def remove(self, eating):
        if self.eatings:
            for e in self.eatings:
                if e.name == eating.name:
                    self.eatings.remove(e)

    def get_all(self):
        return self.eatings

    def get_by_name(self, name):
        if self.eatings:
            for e in self.eatings:
                if e.name == name:
                    return e
        return "Прием пищи не найден"