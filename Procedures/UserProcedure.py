from Repository.UserRepository import UserRepository
from business_rules import validate_user_height, validate_user_weight

class UserProcedure:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def add_user_if_valid(self, user):
        if validate_user_height(user.height) and validate_user_weight(user.weight):
            self.user_repository.add(user)
            print(f'Пользователь "{user.name}" успешно добавлен.')
        else:
            print(f'Ошибка при добавлении пользователя "{user.name}": Рост и вес пользователя должны соответствовать действительности.')

    def find_user_by_name(self, name):
        result = self.user_repository.get_by_name(name)
        if result != "Пользователь не найден":
            print(f'Пользователь "{name}" найден.')
            return result
        else:
            print('Пользователь не найден.')
            return None

    def get_user_by_id(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        if user:
            print(f'Пользователь с ID {user_id} найден: {user.name}.')
        else:
            print(f'Пользователь с ID {user_id} не найден.')
        return user
