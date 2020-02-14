import numpy as np
def factorization():
    p=n
    x=2
    while p < (n + 1):
        if p % x != 0:
            while p % x != 0:
                x += 1
            while p % x == 0:
                list_prime.append(x)
                p = p / x
                while p % x != 0:
                    x += 1
                    if x > p:
                        break
        if p % x == 0:
            while p % x == 0:
                list_prime.append(x)
                p = p / x
                while p % x != 0:
                    x += 1
                    if x > p:
                        break
        p = np.prod(list_prime) + 1
        if p < n:
            break

try:
    print("What number would you like to know the prime number(s) of?")
    n= eval(input())
    list_prime=[]
    factorization()
    print(list_prime)
except:
    print("An error occured")
