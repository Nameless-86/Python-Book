import ctypes


class DynamicArray():
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # Low level array

    def __len__(self):
        """Return the number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return the element at index k"""
        if not 0 <= k < self._n:
            raise IndexError("Invalid index")
        return self._A[k]  # Retreieve from array

    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:  # Not enough room
            self._resize(2 * self._capacity)  # double the capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # Non public utility
        """Resize internal array to capacity c"""
        B = self._make_array(c)  # New bigger array
        for k in range(self._n):  # for each existing balue
            B[k] = self._A[k]
        self._A = B  # Use the bigger array
        self._capacity = c

    def _make_array(self,c): # Non public utility
        """Return new array with capacity c"""
        return(c* ctypes.py_object)() #See ctypes documentation
    

    
array = DynamicArray()
array.append(5)
print(array.__getitem__(0)) # 5
print(array.__getitem__(1)) # error de indice