#!/usr/bin/env python3
"""Module demonstrating mixins with a Dragon class."""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Print swimming ability."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Print flying ability."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining multiple behaviors via mixins."""

    def roar(self):
        """Print dragon roar."""
        print("The dragon roars!")
