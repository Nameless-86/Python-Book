# Import the Node class and typing module
from Node import Node
from typing import Any

# Define the Stack class
class Stack():
    # Constructor to initialize the Stack object
    def __init__(self) -> None:
        # Initialize the top of the stack to None
        self.top = None

    # Push a value onto the top of the stack
    def push(self, value) -> None:
        # Create a new Node with the given value and set its next Node to the current top of the stack
        inVal = Node(value, self.top)
        # Set the top of the stack to the newly created Node
        self.top = inVal

    # Pop the top value off the stack and return it
    def pop(self) -> Any:
        # Check if the stack is empty
        if self.top is None:
            # If it is, return None
            return
        else:
            # Otherwise, store the value of the current top of the stack and its next Node
            valueRet = self.top.getValue()
            nextVal = self.top.getNext()
            # Set the top of the stack to the next Node
            self.top = nextVal
            # Return the value of the original top Node
            return valueRet

    # Return the value of the top Node without removing it from the stack
    def peek(self) -> Any:
        # Return the value of the top Node
        return self.top.getValue()
    
    # Check if the stack is empty
    def isEmpty(self) -> bool:
        # If the top of the stack is None, then it is empty
        return self.top is None