from Node import Node

class Queue():
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        inValue = Node(value, None)

        if self.size == 0:
            self.front = inValue
            self.rear = inValue
        else:
            self.rear.setNext(inValue)
            self.rear = inValue

        self.size += 1

    def dequeue(self):
        if self.size > 0:
            value = self.front.getValue()
            self.front = self.front.getNext()

            self.size -= 1
            return value
        else:
            return
        
    def peek(self):
        return self.front.getValue()
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        return str(self.front.getValue())