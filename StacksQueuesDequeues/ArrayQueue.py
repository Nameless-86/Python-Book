import Empty


class ArrayQueue():
    """FiFo queue implementation using a python list as a underlying storage"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Returns the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Checks if the queue is empty"""
        return self._size == 0

    def first(self):
        """
        Return but dont remove the first element at the front of the queue
        Raise error if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """
        remove and return the first element from the queue
        raise error if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None  # helps with garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an elemento the the back of the queue"""
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        """resize the queue to a new capacity"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
