class Eating:
    def __init__(self, id, user, name):
        self.id = id
        self.user = user
        self.name = name

    def get_info(self):
        return [self.id, self.user, self.name]