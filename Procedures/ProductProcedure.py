from Repository.ProductRepository import ProductRepository
from business_rules import validate_product_name

class ProductProcedure:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def add_product_if_valid(self, product):
        if validate_product_name(product.name):
            self.product_repository.add(product)
            print(f'Продукт "{product.name}" успешно добавлен.')
        else:
            print(f'Ошибка в названии продукта.')
