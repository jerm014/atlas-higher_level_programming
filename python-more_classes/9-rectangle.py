#!/usr/bin/python3
'''This module does rectangle things'''


class Rectangle:
    '''Rectangle class

    Attributes:
        number_of_instances (int): how many rectangle objects
        print_symbol (str): character used to print rectangle
        width (int): width of rectangle
        height (int): height of rectangle
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initializes a rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle

        Raises:
            TypeError: width or height is not an integer
            ValueError: width or height is less than 0
        '''
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        Rectangle.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''compare the area of two rectangles and determine if one is larger

        Args:
            rect_1 (Rectangle): a rectangle to compare
            rect_2 (Rectangle): a rectangle to compare

        Returns:
            Rectangle: larger rectangle between the two or rect_1
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        '''make a rectangle that is a square

        Args:
            size (int): square size

        Returns:
            Rectangle: a square one
        '''
        return cls(size, size)

    @property
    def width(self):
        '''get or set width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width

        Args:
            value (int): width

        Raises:
            TypeError: width is not an integer
            ValueError: width is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''get or set height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''set height

        Args:
            value (int): height

        Raises:
            TypeError: height is not an integer
            ValueError: height is less than 0'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''get area

        Returns:
            int: area
        '''
        return self.__height * self.__width

    def perimeter(self):
        '''get perimeter

        Returns:
            int: perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        '''Prints rectangle to stdout using #

        Returns:
            str: #
        '''
        res = ""
        if self.__width != 0 and self.__height != 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    res += str(self.print_symbol)
                if h < self.__height - 1:
                    res += "\n"

        return res

    def __repr__(self):
        '''Returns the width and height

        Returns:
            str: Rectangle(width, height)
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''Print message when a rectangle is deleted'''
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
