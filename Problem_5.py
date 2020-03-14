#Numpy is used for finding product of arrays
import numpy as np

#Same function used for project Euler 3 to find prime factorization
def factorization():
    global prime_temp
    prime_temp=[]
    p=n
    x=2
    while p % x != 0:
        x += 1
    while p % x == 0:
        prime_temp.append(x)
        p = p / x
        while p % x != 0:
            x += 1
            if x > p:
                break
#After finding factors this function finds where a number x occured the most
#It then multiplies the number x where it occured most in the array to other
#Prime Numbers that occured the most.
#Don't recall the algorithm name
def sorting():
    for x in range(2,max(maximum)+1):
        temp_list=[]                            #Used to store arrays for short time.
        for y in range (0,len(list_prime)):
            turtle=list_prime[y]                #Turtles used as temporary variables
            turtle1=turtle.count(x)             #Why turtles well because turtles
            turtle2=x**(turtle1)
            temp_list.append([turtle2])         #This is used to find maximum times a number is an array. On the plus side it filters out 0 because anything to the exponent 0 is 1.
        mult_list.append(max(temp_list))


print("What least common multiple of number 1-n(your number) would you like to know?")
input= eval(input())
list_prime=[]
mult_list=[]
for n in range (2,input+1):
    factorization()
    list_prime.append(prime_temp)
maximum=max(list_prime)
sorting()
print("The least common multiple is",np.product(mult_list))
