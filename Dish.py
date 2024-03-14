class Dish:
    def __init__(self, id, name, calorifik, protein, fat, carb):
        self.id = id
        self.name = name
        self.calorifik = calorifik
        self.protein = protein
        self.fat = fat
        self.carb = carb

    def get_info(self):
        return [self.id, self.name, self.calorifik, self.protein, self.fat, self.carb]