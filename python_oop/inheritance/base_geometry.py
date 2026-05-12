#!/usr/bin/env python3
"""Module that defines a BaseGeometry class."""


class BaseGeometry:
    """Base class for geometric objects."""

    def area(self):
        """Not implemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
