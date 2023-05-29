class TreeNode():
    def __init__(self, value):
        # Initialize left and right child nodes to None and set node value
        self.left = None
        self.right = None
        self.content = None
        self.value = value

    def insert(self, value, content=None):
        # If the new value is less than the current node's value
        if value < self.value:
            # If there is no left child node, create a new one with the new value
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            # If there is a left child node, recursively call the insert method on it
            else:
                self.left.insert(value, content)
        # If the new value is greater than or equal to the current node's value
        else:
            # If there is no right child node, create a new one with the new value
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            # If there is a right child node, recursively call the insert method on it
            else:
                self.right.insert(value, content)

    def inorder_traversal(self):
        # Traverse the left subtree recursively
        if self.left:
            self.left.inorder_traversal()
        # Visit the current node
        print(self.value)
        # Traverse the right subtree recursively
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        # Visit the current node
        print(self.value)
        # Traverse the left subtree recursively
        if self.left:
            self.left.preorder_traversal()
        # Traverse the right subtree recursively
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        # Traverse the left subtree recursively
        if self.left:
            self.left.postorder_traversal()
        # Traverse the right subtree recursively
        if self.right:
            self.right.postorder_traversal()
        # Visit the current node
        print(self.value)

    def find(self, value):
        # If the value we're looking for is less than the current node's value
        if value < self.value:
            # If there is no left child node, the value is not in the tree
            if self.left is None:
                return None
            # If there is a left child node, recursively call the find method on it
            else:
                return self.left.find(value)
        # If the value we're looking for is greater than the current node's value
        elif value > self.value:
            # If there is no right child node, the value is not in the tree
            if self.right is None:
                return None
            # If there is a right child node, recursively call the find method on it
            else:
                return self.right.find(value)
        # If the value we're looking for is equal to the current node's value, return the node's value
        else:
            return self


if __name__ == '__main__':
    tree = TreeNode(6)
    tree.insert(5)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.insert(2)
    tree.insert(4)
    tree.insert(19, {"data": "Hello Friend"})
    tree.insert(29)
    tree.insert(11)
    tree.insert(4)
    tree.insert(2)
    # print(tree.left.left.left.right.value)
    print(tree.find(19).content["data"])
    print(tree.find(19).content)
