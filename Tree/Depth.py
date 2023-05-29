def depth(self, p):
    """Return the number of levels separation position p from the root"""
    if self._isroot(p):
        return 0
    else:
        return 1 + self.depth(self.parent(p))
