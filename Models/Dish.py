class Dish:
    def __init__(self, id, name, calorifik, protein, fat, carb, products, category):
        self.id = id
        self.name = name
        self.calorifik = calorifik
        self.protein = protein
        self.fat = fat
        self.carb = carb
        self.products = products
        self.category = category

    def get_info(self):
        return [self.id, self.name, self.calorifik, self.protein, self.fat, self.carb, self.products, self.category]

    def __eq__(self, other):
        if isinstance(other, Dish):
            return (self.id == other.id and
                    self.name == other.name and
                    self.calorifik == other.calorifik and
                    self.protein == other.protein and
                    self.fat == other.fat and
                    self.carb == other.carb and
                    self.products == other.products and
                    self.category == other.category)
        return False