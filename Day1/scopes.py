username ="decoder"

def test():
    username = "coder"
    print(username)

print(username)
test()


x=100

def func2(y):
    z=x+y
    return z

result = func2(10)
print(result) 


#closure
def outer_func(x):
    def inner_func(y):
        return x+y
    return inner_func

result = outer_func(10)
print(result(20))
 

