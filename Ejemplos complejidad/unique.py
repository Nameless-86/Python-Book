def unique1(S):
    """Return true if there are no duplicate elements in S"""
    for j in range(len(S)):
        for k in range(j+1, len(S)):
            if S[j] == S[k]:
                return False
        return True

def unique2(S):
    """Return true if there are no duplicate elements in S"""
    temp = sorted(S)
    for j in range(1,len(temp)):
        if S[j-1] == S[j]:
            return False
    return True