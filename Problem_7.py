import math
def prime_range():
    p=11
    while len(list_prime)<n+1:
        true = 0
        x = math.ceil(math.sqrt(p))
        c=2
        while c<=x:
            if p%c==0:
                true=1
                break
            c+=1
        if true==0:
            list_prime.append(p)
        p+=1

print("What is your number?")
n=eval(input())
list_prime=[1,2,3,5,7]          ###To speed up process###
prime_range()
print(list_prime)
print("The",n,"prime number is", list_prime[n])


