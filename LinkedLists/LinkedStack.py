from ..StacksQueuesDequeues import Empty


class LinkedStack():
    """"Lifo stack implementation using a singly linked list forr storage"""

    # --------------------------------Nested _node Class--------------------------------
    class _Node():
        """Lightweight nonpublic class for stroing singly linked node"""
        __slots__ = 'element', 'next'  # Streamline memory usage

        def __init__(self, element, next):  # initialization of nodes fields
            self._element = element  # reference to users element
            self._next = next  # reference to next node

    # --------------------------------stack methods--------------------------------
    def __init__(self):
        """Create an empty stack"""
        self._head = None  # reference to the head node
        self._size = 0  # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Check if the stack is empty"""
        return self.size == 0

    def push(self, e):
        """Add element to the stack"""
        self._head = self.Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """Return but dont remove top element from the stack
        Raise empty exception if stack is empty"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element  # top of stack is at head of list

    def pop(self):
        """
        remove and return top element from the stack
        raise Empty exception if stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(6)
    stack.push(6)
    stack.push(6)
    stack.push(6)
    stack.push(6)
    stack.push(6)
    