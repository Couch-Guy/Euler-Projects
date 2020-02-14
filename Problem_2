def Fibonacci():
    global n
    a=1
    b=0
    c=0
    while c < n:
        c=a+b
        a=b
        b=c
        if c % 2 ==0:
          list_c.append(c)


try:
    print("Input what number you would like to find the Fibonacci number up to.")
    n= eval(input())
    list_c = []
    Fibonacci()
    print(list_c)
    print(sum(list_c))

except:
    print("An error occurred")
