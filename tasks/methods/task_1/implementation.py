class Coffee:
    def __init__(self, *extra):
        self.ingredients = ['water', 'coffee'] + list(extra)

    @classmethod
    def get_cappuccino(cls):
        coffee = Coffee('milk')
        return coffee

    @classmethod
    def get_latte(cls):
        coffee = Coffee('syrup')
        return coffee

    @classmethod
    def get_glace(cls):
        coffee = Coffee('ice-cream')
        return coffee


cappuccino = Coffee.get_cappuccino()
print(cappuccino.ingredients)
