ass Bottle:
    def __init__(self, color):
        self.color = color
        self.contains = 0

    def get_content(self):
        return self.contains

    def fill(self, volume):
        return self.contains == volume + self.contains


bottle_1 = Bottle('синяя')
bottle_2 = Bottle('красная')

print(bottle_1.color, bottle_1.get_content())
bottle_1.fill(100)
print(bottle_1.color, bottle_1.get_content())
