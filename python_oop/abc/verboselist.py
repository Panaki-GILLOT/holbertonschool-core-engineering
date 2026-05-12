#!/usr/bin/env python3
"""Module that defines VerboseList, a list with notifications."""


class VerboseList(list):
    """A list that prints messages when modified."""

    def append(self, item):
        """Add an item to the list and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print number of items added."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove item from list and print a message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop item from list and print a message."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
