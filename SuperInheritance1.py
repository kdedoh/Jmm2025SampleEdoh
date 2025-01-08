# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 17:40:41 2023

@author: kdedo
"""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
#####################################################################
class Cube(Square):
    def surface_area(self):
        #face_area = super().area()
        face_area = super(Square,self).area()
        return face_area * 6

    def volume(self):
        #face_area = super().area()
        face_area = super(Square,self).area()
        return face_area * self.length


#####################################################################
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area() # Square
        perimeter = super().perimeter()   #Square
        return 0.5 * perimeter * self.slant_height + base_area





square = Square(4)
print(square.area())

rectangle = Rectangle(4,3)
print(rectangle.area())

cube = Cube(3)
print('Cube surface',cube.surface_area())
print('Cube volume',cube.volume())

pyramid = RightPyramid(2, 4)
print('Pyramid area', pyramid.area())