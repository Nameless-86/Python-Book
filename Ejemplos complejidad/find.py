def find(S, val):
    """Return index j such that S[j] == val"""
    n = len(S)
    j = 0
    while j < n:
        if S[j] == val:
            return j
        j += 1
    return -1
