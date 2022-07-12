#!/usr/bin/python3
"""
    Module for Rectangle  sub-class
"""


from models.base import Base


class Rectangle(Base):
    """
        Rectangle class created as a subclass
        of the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            initialize sub class Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            get value of class instance property width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            set value of class instance property width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            get value of class instance property height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            set value of class instance property height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            get value of class instance property x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            set value of class instance property x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            get value of class instance property y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            set value of class instance property y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            returns the area of the class instance
        """
        return self.width * self.height

    def display(self):
        """
            prints the dimension of class instance shape with respect
            to spatial parameters
        """
        [print() for v in range(self.y)]
        for h in range(self.__height):
            [print(" ", end="") for h in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print()
        # [[print("#", end="") for w in range(self.
        # __width)] print() for h in range(self.__height)]

    def __str__(self):
        """
            string representation of Rectangle class instance
        """
        return "[{}] ({}) {}/{} - {}/{}" \
            .format(self.__class__.__name__, self.id, self.x,
                    self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
            updates propeties of a class instance
            with args or kwargs if args is not passed
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
            converts properties of
            class instance to a dictionary
        """
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["width"] = self.width
        my_dict["height"] = self.height
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
