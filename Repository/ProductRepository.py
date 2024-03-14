from Repository import FakeRepository

class ProductRepository(FakeRepository.FakeRepository):

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        if self.products:
            for p in self.products:
                if p.name == product.name:
                    self.products.remove(p)

    def get_all(self):
        return self.products

    def get_by_name(self, name):
        if self.products:
            for p in self.products:
                if p.name == name:
                    return p
        return "Продукт не найден"