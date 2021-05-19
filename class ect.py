# explanation
class Shapes:
    def __init__(self, name, sides):
        self.name=name
        self.sides=sides

    def Area(self):
        print("I am a :" + self.name + "\n" + "I have " + self.sides + "Sides")

obj_shapes=Shapes("Shape", "so many ")
obj_shapes.Area()

class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length=len1
        self.width=wid1
    def Area(self):
        result=self.length * self.width
        return result
obj_book=Rectangle(10, 15)
print(obj_book.Area())
obj_screen=Rectangle(15,8)
print(obj_screen.Area())

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base=base
        self.height=height
    def Area(self):
        result = self.base / 2 *self.height
        return result
obj_tri=Triangle(15, 10)
print(obj_tri.Area())

class Circle(Shapes):
    def __init__(self, name, side, radius):
        super().__init__(name, side)
        self.radius=radius
    def Area(self):
        import math
        result = math.pi * self.radius* self.radius
        return result
obj_coin = Circle("name", "shape", 7)
print(obj_coin.Area())
