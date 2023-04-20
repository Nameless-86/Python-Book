def bad_fibo(n):
    if n == 0 or n == 1:
        return n
    return (bad_fibo(n - 1) + bad_fibo(n - 2))


print(bad_fibo(7))


def good_fibo(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibo(n - 1)
        return (a+b, a)
    
print(good_fibo(7))


n1, n2 = 0, 1
for i in range(6):
    nth = n1+n2
    n1 = n2
    n2 = nth
print(n2)
