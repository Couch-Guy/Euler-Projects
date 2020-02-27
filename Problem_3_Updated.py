#This is an update with reduced coding for easier intgration in future projects

def factorization():
    p=n
    x=2
    while p % x != 0:
        x += 1
    while p % x == 0:
        list_prime.append(x)
        p = p / x
        while p % x != 0:
            x += 1
            if x > p:
                break

try:
    print("What number would you like to know the prime number(s) of?")
    n= eval(input())
    list_prime=[]
    factorization()
    print(list_prime)
except:
    print("An error occured")
