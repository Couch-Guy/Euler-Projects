def factorization():
    p=1
    while len(list_prime)<n:
        x = 2
        p += 1
        while x<=p:
            if p==x:
                list_prime.append(x)
                break
            if p%x==0:
                break
            x += 1

print("What is your number?")
n=eval(input())
list_prime=[]
factorization()
print(list_prime)
print("The",n,"prime number is", list_prime[n-1])
