def prefix_average3(S):
    n = len(S)
    A = [0] * n
    total = 0

    for j in range(n):
        total += S[j]
        A[j] = total / (j+1)
    return A

a = [2,3,4,5,6]
print(prefix_average3(a))