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


class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def __str__(self):
        return f"{self.color} circle with middle at {self.x, self.y} and {self.radius} radius"

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


circle = Circle(3, 4, "orange", 12)
print(circle)
print(circle.area())
print(circle.perimeter())

