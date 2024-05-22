from Repository.EatingRepository import EatingRepository
from business_rules import validate_eating_name

class EatingProcedure:
    def __init__(self, eating_repository: EatingRepository):
        self.eating_repository = eating_repository

    def add_eating_if_valid(self, eating):
        if validate_eating_name(eating.name):
            self.eating_repository.add(eating)
            print(f'Прием пищи "{eating.name}" успешно добавлен.')
        else:
            print(f'Ошибка в названии приема пищи.')
