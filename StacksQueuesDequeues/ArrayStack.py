import Empty


class ArrayStack():
    """LIFO stack implementation using python list as underlying storage"""

    def __init__(self):
        """Create empty stack"""
        self._data = []  # non public list instance

    def len(self):
        """Return the number of elements in the stack"""
        return len(self._data)

    def isEmpty(self):
        """Check if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """add element e to the top of the stack"""
        self._data.append(e)  # new item stored at end of list

    def top(self):
        """
        Return bot do not remove the element at the top of the stack
        Raise empty stack exception if the stack is empty        
        """

        if self.isEmpty():
            raise Empty("Stack is empty")
        return self._data[-1]  # Last element in the list

    def pop(self):
        """
        Remove and return the top element from the stack
        Raise empty stack exception if the stack is empty
        """
        if self.isEmpty():
            raise Empty("stack is empty")
        return self._data.pop()  # remove last element from the list
    
    def __str__(self):
        return f"{self._data}"


if __name__ == "__main__":
    stack = ArrayStack()
    print(stack)
    stack.push(5)
    stack.push(8)
    stack.push(10)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    print(stack.isEmpty())
