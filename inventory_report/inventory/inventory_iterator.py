from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, inventory):
        self._inventory = inventory
        self._index = 0

    def __next__(self):
        if self._index < len(self._inventory.data):
            product = self._inventory.data[self._index]
        else:
            raise StopIteration
        self._index += 1
        return product
