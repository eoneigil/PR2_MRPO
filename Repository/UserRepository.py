from Repository import FakeRepository


class UserRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def remove(self, user):
        if self.users:
            for u in self.users:
                if u.name == user.name:
                    self.users.remove(u)

    def get_all(self):
        return self.users

    def get_by_name(self, name):
        if self.users:
            for u in self.users:
                if u.name == name:
                    return u
        return "Пользователь не найден"