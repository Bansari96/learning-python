# Example for function in python
#basic function
def func1():
    print("Inside the function 1")

func1()
print(func1()) # first it print the function output and for the print statement execution, func1 does not returning any value so it will print "None"
print(func1) # printing the value of the function definition itself

#function with argument and returning value
def func2(arg1, arg2):
    print(arg1, " ", arg2)

def cube(x):
    return x*x*x

func2(10,20)
print(func2(10,20))
print(cube(3))

#fucntion with arg predefined value, changing order of parameter while calling function
def power(num, x=1):
    result=1
    for i in range(x):
        result=result * num
    return result

print(power(2))
print(power(2,3))
print(power(x=3, num=2))

#function with variable number of arguments
def multi_add(*args):
    result=0
    for x in args:
        result = result + x
    return result

print(multi_add(4,7,2,10,15))