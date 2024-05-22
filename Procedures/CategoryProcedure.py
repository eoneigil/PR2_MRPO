from Repository.CategoryRepository import CategoryRepository
from business_rules import validate_category_name

class CategoryProcedure:
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def add_category_if_valid(self, category):
        if validate_category_name(category.name):
            self.category_repository.add(category)
            print(f'Категория "{category.name}" успешно добавлена.')
        else:
            print(f'Ошибка в названии категории.')
