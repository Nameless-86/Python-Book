
# -------------------------------- _node Class--------------------------------
class _Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

    # --------------------------------List--------------------------------


class LinkedList():

    def __init__(self):
        self.head = _Node()

    def append(self, data):
        new_node = _Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node= cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, k):
        if k>= self.length():
            raise IndexError("Out of range")
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == k:
                return cur_node.data
            cur_idx +=1


if __name__ == "__main__":
    lista = LinkedList()
    lista.append(5)
    lista.display()
    lista.append(15)
    # lista.append(25)
    # lista.append(35)
    lista.display()