from functools import wraps

def flip(func):
    @wraps(func)
    def newfunc(*args):
        print("args:")
        print(*args)
        return func(*args[::-1])
    return newfunc

def divide(a,b):
    return a/b

new_divide = flip(divide)
a = new_divide(10.0, 30.0)
print(a)
