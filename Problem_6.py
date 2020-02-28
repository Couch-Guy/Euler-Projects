def adding_natural():
    sum_of=0
    for x in range(1,number+1):
        sum_of+=x
    sum_of=sum_of**(2)
    return sum_of
def mult_natural():
    multi=0
    for x in range(1,number+1):
        multi= multi + (x**(2))
    return multi

try:
    print("Choose your number")
    number=eval(input())
    print(adding_natural()-mult_natural())
except:
    print("An error occured")
