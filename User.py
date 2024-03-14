class User:
    def __init__(self, id, age, gender,  weight, name, activity):
        self.id = id
        self.age = age
        self.gender = gender
        self.weight = weight
        self.name = name
        self.activity = activity

    def get_info(self):
        return [self.id, self.age, self.gender, self.weight, self.name, self.activity]