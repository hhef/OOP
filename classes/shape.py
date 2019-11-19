class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"{self.color} figure with middle at {self.x, self.y}"

    def describe(self):
        print(self.x, self.y, self.color)

    def distance(self, another_shape):
        return ((self.x - another_shape.x) ** 2 + (self.y - another_shape.y) ** 2) ** 0.5


shape = Shape(0, 0, "black")
shape1 = Shape(3, 4, "orange")

shape1.describe()
print(shape1)
shape.describe()
print(shape)
print(shape.distance(shape1))
