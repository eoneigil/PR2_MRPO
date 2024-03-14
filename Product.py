class Product:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return [self.name]