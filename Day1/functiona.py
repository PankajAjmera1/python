#basic syntax
def sqare_of_number(n):
    print( n**2  )

result =sqare_of_number(5) 
print(result)  #none

import math

def circle_stats(r):
    area = math.pi * r**2
    circumference = 2 * math.pi * r
    return area, circumference

result_of_area ,result_of_circum = circle_stats(5)

print(result_of_area)
print(result_of_circum)

#round_off to 2 decimal places  
print(round(result_of_area,2))
print(round(result_of_circum,2))


#lamda function
#lambda arguments : expression
#lambda function is a small anonymous function

cube = lambda x : x**3
print(cube(3))


#*args
def add(*args):
    return sum(args)

print(add(1,2,3,4,5))



#**kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, b=2, c=3)


#generators function with yield
def even_generator(limit):
    for i in range(0,limit+1,2):
        yield i  #return a value and pause the function

  
for i in even_generator(10):
    print(i)    


#recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


#decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
