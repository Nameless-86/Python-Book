####
#Linear
#
def is_prime1(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return "Wrong input"


print(is_prime1(5))

print(is_prime1(3))

print(is_prime1(1))

print(is_prime1(4))
##################################################
##################################################
##################################################
##################################################
#complejidad sqrt(n)
import math as mt

def is_prime2(n):
    asd = int(mt.sqrt(n))
    if n > 1:
        for i in range(2, asd+1):
            if (n % i) == 0:
                return False
        return True
    else:
        return "Wrong input"

print(is_prime2(5))

print(is_prime2(3))

print(is_prime2(1))

print(is_prime2(4))