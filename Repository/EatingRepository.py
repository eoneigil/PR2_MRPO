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

    def get_all_meals_for_user(self, user):
        meals_for_user = []
        for eating in self.eatings:
            if eating.user == user:
                meals_for_user.append(eating)
        return meals_for_user