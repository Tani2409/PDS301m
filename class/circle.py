import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

radius = int(input("Enter radius: "))
circle = Circle(radius)
print(f"area:{circle.area().f} ") 
print(f"perimeter:{circle.perimeter().f} ")