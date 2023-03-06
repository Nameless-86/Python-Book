def fibo(n):
    if n == 0 or n == 1:
        return n
    return (fibo(n - 1) + fibo(n - 2))


print(fibo(7))


n1, n2 = 0, 1
for i in range(6):
    nth = n1+n2
    n1 = n2
    n2 = nth
print(n2)
