class Coffee:
    def __init__(self):
        self.ingredients = ['coffee', 'water']

    def get_cappuccino(self):
        self.ingredients = ['coffee', 'water', 'milk']
        return self

    def get_latte(self):
        self.ingredients = ['coffee', 'water', 'syrup']
        return self

    def get_glace(self):
        self.ingredients = ['coffee', 'water', 'ice-cream']
        return self


cappuccino = Coffee().get_cappuccino()
print(cappuccino.ingredients)
