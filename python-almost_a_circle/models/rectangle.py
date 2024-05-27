#!/usr/bin/python3
"""File for class Rectangle, which inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle, inherits from class Base"""
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """Initialize a rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.__x = value
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.__y = value
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """return the area of this rectangle"""
        return self.__width * self.__height

    def display(self):
        """print this rectangle"""

        for y in range(0, self.__y):
            print()
        for h in range(0, self.__height):
            print(" " * self.__x, end="")
            for w in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """print out a rectangle (or a square)"""
        s = "[" + type(self).__name__ + "] (" + str(self.id) + ") "
        s += str(self.__x) + "/" + str(self.__y) + " - "
        if type(self).__name__ == "Rectangle":
            s += str(self.__width) + "/" + str(self.__height)
        else:
            s += str(self.__width) 
        return s

    def update(self, *args, **kwargs):
        """"update the Rectangle"""
        if type(self).__name__ == "Rectangle":
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[1]
                self.__x = args[2]
                self.__y = args[3]
            except IndexError:
                pass

        if kwargs is not None and args is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
                elif key == "size":
                    self.__width = value
                    self.__height = value
