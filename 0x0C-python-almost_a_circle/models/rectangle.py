#!/usr/bin/python3
"""Defines a rectangle class"""
from base import Base


class Rectangle(Base):
    """Rectangle object inherit from Base cls"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """ Initialize a new rectangle
        Args:
        width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def validator(method, val):
        """ check if type of val"""
        if type(val) is not int:
            raise TypeError(f"{method} must be an integer")

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        self.validator("width", val)
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        self.validator("height", val)
        if val <= 0:
            raise ValueError("height must be >0")
        self.__height = val

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, val):
        self.validator("x", val)
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, val):
        self.validator("y", val)
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """function to represent triangle by #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return id x/y width/high"""
        repres = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width,
                                                         self.height)
        return repres

    def update(self, *args, **kwargs):
        """Update rectangle attributes
        Args:
            *args list of values
            1- id
            2- width
            3- height
            4- x
            5- y

            **kwargs (dict): New key/value pairs of attributes.
            """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
