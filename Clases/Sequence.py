from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        """Returns the number of elements in the sequence
        """

    @abstractmethod
    def __getitem__(self, j):
        """Returns the element at index j in the sequence"""

    def __contains__(self, val):
        """Returns True if val found in the sequence"""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def index(self, val):
        """Return leftmost index at val is found"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError("Value not found in sequence")

    def count(self, val):
        """return number of elements equal to given value"""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

