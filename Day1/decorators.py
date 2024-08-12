
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result =func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start} seconds")
        return result
    return wrapper

@timer
def example(n):
    time.sleep(n)

#ye example function se hokar jata hai

example(2)



#2

def cache(func):
    cahe_value ={}

    def wrapper(*args):
        
        if args  in cahe_value:
            return cahe_value[args]
        result = func(*args)
        cahe_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(2)
    return a+b

print(long_running_function(1,2))
print(long_running_function(2,2))

