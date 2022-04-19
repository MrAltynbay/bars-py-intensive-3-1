class Flower(object):
    def __init__(self, color):
        self.color = color


class FlowerFactory:
    flowers = {}

    @staticmethod
    def get_flower(color):
        return FlowerFactory.flowers.setdefault(color, Flower(color))


class RowOfFlowerBed(object):
    def __init__(self, row_number):
        self.row_number = row_number

    def plant(self, flower):
        print("Plant {} flower on row {}".format(flower.color, self.row_number))


class FlowerBed(object):
    def __init__(self):
        self.flower_planted = 0
        self.rows = {}

    def get_row(self, number):
        return self.rows.setdefault(number, RowOfFlowerBed(number))

    def plant_on_flower_bed(self):
        self.plant_flower('red', 1)
        self.plant_flower('blue', 1)
        self.plant_flower('yellow', 1)
        self.plant_flower('red', 2)
        self.plant_flower('blue', 2)
        self.plant_flower('yellow', 2)
        self.plant_flower('red', 3)
        self.plant_flower('blue', 3)
        self.plant_flower('yellow', 3)
        self.plant_flower('red', 4)
        self.plant_flower('blue', 4)
        self.plant_flower('yellow', 4)

    def plant_flower(self, color, row_number):
        self.get_row(row_number).plant(FlowerFactory.get_flower(color))
        self.flower_planted += 1


if __name__ == '__main__':
    FlowerBed().plant_on_flower_bed()
