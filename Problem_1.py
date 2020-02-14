#Problem 1 From Project Euler
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    #The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
import numpy as np


def loop_x(): #This function is used to find the multiples of x before 1000
    global x #Global is used to tell function to use the global x intiger instead of local
    global x1
    r1=1
    x1=0
    while x1 < 1000:
        x1=x*r1
        r1 += 1
        if x1<1000: #This if statement stops x from going over 1000 and used as saftey measure
            list_x.append(x1)
        else:
            break
def loop_y(): #This function is used to find the multiples of x before 1000
    global y
    global y1
    r2=1
    y1=0
    while y1<1000:
        y1= y*r2
        r2 +=1
        if y1<1000:
            list_y.append(y1)
        else:
            break


try:
    print("Pick first multiple.")
    x= eval(input()) #This is required to input intiger not string
    print("Pick second multiple.")
    y= eval(input())
    list_x = [] #Creating an array to store values
    list_y = []
    loop_x()
    loop_y()
    Multiple_Sum= sum(sorted(np.unique(list_x+list_y))) #sorted(np.unique(list_x+list_y)) isused to get rid of duplicate arrrays and the sum() is used to add the arrays
    print("The sum of the multiples is " ,Multiple_Sum)

except:
    print("Error Occured")
