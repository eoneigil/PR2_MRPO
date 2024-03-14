class Dish:
    def __init__(self, id, name, calorifik, protein, fat, carb, products):
        self.id = id
        self.name = name
        self.calorifik = calorifik
        self.protein = protein
        self.fat = fat
        self.carb = carb
        self.products = products

    def get_info(self):
        return [self.id, self.name, self.calorifik, self.protein, self.fat, self.carb, self.products]