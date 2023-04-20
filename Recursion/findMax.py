def find_max(S):
    """Find the maximum in a given list"""
    if len(S) == 1: #Base case
        return S[0]
    else:
        max_val = find_max(S[1:]) #Recursive case
        if S[0] > max_val:
            return S[0]
        else:
            return max_val


print(find_max([1, 3, 5, 7, 8, 9, 10]))