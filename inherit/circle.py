from classes.shape import Shape


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
