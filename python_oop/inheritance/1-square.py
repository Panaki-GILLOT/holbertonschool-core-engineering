#!/usr/bin/env python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class (special case of Rectangle)."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        width = self._Rectangle__width
        height = self._Rectangle__height
        return width * height

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Rectangle] {self._Rectangle__width}/" \
               f"{self._Rectangle__height}"