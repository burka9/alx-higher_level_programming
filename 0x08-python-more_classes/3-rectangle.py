#!/usr/bin/python3
"""this is a comment"""


class Rectangle:
    """this is a rectangle class"""

    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the permieter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ('')

        str = []
        for i in range(self.height):
            [str.append('#') for j in range(self.width)]
            if i != self.height-1:
                str.append('\n')
        return ''.join(str)
