def reverse_string(S):
    if len(S) == 0:
        raise ValueError("String is empty")
    else:
        if len(S) == 1:
            return S
        else:
            return S[-1]+reverse_string(S[:-1])


S = "Hello"
print(reverse_string(S))
