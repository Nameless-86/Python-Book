class SequenceIterator:
    """An iterator for any of pythons sequence types"""

    def __init__(self, sequence):
        self._seq = sequence  # Keep a reference to the data
        self._k = -1  # will increment to 0 on first call

    def __next__(self):
        """Return next element of the sequence or raise StopIteration error"""
        self._k += 1 #Advance to next index
        if self._k < len(self._seq):
            return (self._seq[self._k]) #Return the data element
        else:
            raise StopIteration() #There are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
