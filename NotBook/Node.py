class Node:
    """class for basic node structure"""
    def __init__(self,value,next):
        self.value = value
        self.next = next

    def getValue(self):
        """returns the value of the node"""
        return self.value
    
    def getNext(self):
        """returns the value of the next node"""
        return self.next
    
    def setValue(self,value):
        """Sets the value of the node"""
        self.value = value

    def setNext(self,next):
        """
        Links the node to another
        You can use self.next = None to make end of list
        """
        self.next = next

    def __str__(self):
        return str(self.value)
