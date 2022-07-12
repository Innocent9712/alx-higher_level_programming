#!/usr/bin/python3
"""
    Module for Square sub-class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class created as a subclass
        of the Rectangle class, which is also a subclass
        of the Base Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            initialize sub class Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            get value of class instance property size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            set value of class instance property size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
            string representation of Square class instance
        """
        return "[{}] ({}) {}/{} - {}" \
            .format(self.__class__.__name__, self.id,
                    self.x, self.y, self.size)

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
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
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
        my_dict["size"] = self.size
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict
