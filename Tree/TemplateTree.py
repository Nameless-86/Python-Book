class Tree():
    """Abstract base class for tree structures"""
    class Position():
        """An abstraction representing the location of a single element"""

        def element(self):
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self, other):
            """Return true if other position represents the same location"""
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self, other):
            """Return true if other position represents the same location"""
            raise NotImplementedError("Must be implemented by subclass")

    def root(self):
        """Return Position representing the trees's root or none if empty"""
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self, p):
        """Return position representing p's parents or none if p is root"""
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children position p has"""
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        """generate an iteration of positions representing p's children"""
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """Return total number of elemnets in the tree"""
        raise NotImplementedError("Must be implemented by subclass")

    # Concrete methods implemented in this class

    def is_root(self, p):
        """Return true if position p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return true if position does not have any children"""
        return self.num_children() == 0

    def is_empty(self):
        """Return true if the tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separation position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):  # Works but O(n^2)
        """Return the height of the tree"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):  # Works O(n)
        """Return the height of the subtree rooted at position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """
        Return the height of the subtree rooted at position p
        If p is none return the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self._height2(p)  # start height2 recursion
