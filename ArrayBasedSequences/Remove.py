def remove(self, value):
    """Remove first occurrence of value or raise value error"""
    # The array will not shrink after this operation
    for k in range(self._n):
        if self._A[k] == value:  # Found match
            for j in range(k, self._n - 1):  # Shit to fill gap
                self._A[k] = self._A[j+1]
            self._A[self._n-1] = None  # Helps with garbage collection
            self._n -= 1  # We have one less item
            return  # Exit
    raise ValueError("Value not found")  # only reach if no match
