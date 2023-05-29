from TemplateTree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""

    # --------------------additional abstract methods-----------

    def left(self, p):
        """
        Returns a position representing p's left child
        
        returns none if p does not have a left child
        """
        raise NotImplementedError('Must be implemented by subclass')

    def right(self, p):
        """
        Returns a position representing p's right child

        returns none if p does not have a right child
        """
        raise NotImplementedError('Must be implemented by subclass')

    # --------- concrete methods for this class ------------------------

    def sibling(self, p):
        """Return a position representing p's sibling or none if no sibling"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly none
            else:
                return self.left(parent)  # possibly none

    def children(self, p):
        """Generate an iteration of positions representing p's children"""
        if self.left(p) is None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
