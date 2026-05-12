#!/usr/bin/env python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class (special case of Rectangle)."""

    def __init__(self, size):
        """Initialize a square with validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
