from ..StacksQueuesDequeues import Empty


class LinkedQueue():
    """Fifo queue implementation using a singly linked list for storage"""

    # --------------------------------Nested _node Class--------------------------------
    class _Node():
        """Lightweight nonpublic class for stroing singly linked node"""
        __slots__ = 'element', 'next'  # Streamline memory usage

        def __init__(self, element, next):  # initialization of nodes fields
            self._element = element  # reference to users element
            self._next = next  # reference to next node

    # --------------------------------queue methods--------------------------------

    def __init__(self):
        """Create empty queue"""
        self._head = None
        self._tail = None
        self._size = 0  # number of queue elements

    def __len__(self):
        """Return length of the queue"""
        return self._size

    def is_empty(self):
        """Check if queue is empty"""
        return self._size == 0

    def first(self):
        """
        Return but dont remove the first element of the queue
        Raise empty if queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element  # Front aligned with head of list

    def dequeue(self):
        """
        Remove and return the first element of the queue(FIFO)
        Raise empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # special case as queue is empty
            self._tail = None  # removed head had been the tail
        return answer

    def enqueue(self, e):
        """Add element to the back of the queue"""
        newest = self._node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
