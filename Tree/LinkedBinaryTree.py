from BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    class _Node:  # lightweight nonpublic class for storing a node
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstract representation the location of a single element"""

        def __init__(self, container, node):
            """Constructor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """Return element stored at this position"""
            return self._node._element

        def __eq__(self, other):
            """Return true if other is a position representing the same position"""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """return associated node if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return position instance for given node"""
        return self.Position(self, node) if node is not None else None

    # --------binary tree constructor------

    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    # ------public accessors--------

    def __len__(self):
        """Return the total number of elements in the tree"""
        return self._size

    def root(self):
        """Return the root position of the tree (or none if tree is empty)"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the position of p's parent (or none if tree is root)"""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the position of p's left (or none if no left child)"""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the position of p's right (or none if no right child)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of postion p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:  # left child exist
            count += 1
        if node._right is not None:  # right child exist
            count += 1
        return count

    def _add_root(self, e):
        """
        Place element e at the root of an empty tree and return new Position
        Raise ValueError if tree is nonempty
        """

        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """
        Create a new left child for position p, storing element e
        Return position of new node
        Raise value error if position p is invalid or p has already a left child
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("left child exists")
        self._size += 1
        node._left = self._Node(e)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """
        Create a new right child for position p, storing element e
        Return position of new node
        Raise value error if position p is invalid or p has already a right child
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e)
        return self._make_position(node._right)
