def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a python list"""

    if low > high:
        return False
    else:
        mid = (low + high) //2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            #Recur on the portion left of the middle
            return binary_search(data, target, low, mid -1)
        else:
            #Recur on the portion right of the middle
            return binary_search(data, target, mid+1, high)