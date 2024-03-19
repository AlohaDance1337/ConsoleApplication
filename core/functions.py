import math

def sum(a:int|float=None,b:int|float=None):
    return a+b

def mul(a:int|float=None,b:int|float=None):
    return a*b

def div(a:int|float=None,b:int|float=None):
    return a/b

def div_ex(a:int|float=None,b:int|float=None):
    return a//b

def dif(a:int|float=None,b:int|float=None):
    return a-b

def sqrt(a:int|float=None):
    return math.sqrt(a)

def exp(a:int|float=None):
    return math.exp(a)

def module(a:int|float=None):
    return abs(a)

def factorial(a:int=None):
    if a==1:
        return 1
    return factorial(a-1)*a

def log(a:int|float=None,b:int=None):
    return math.log(a,b)

def ln(a:int|float=None)->float:
    return math.log(a,math.e)

def fibonacci(a:int=None):
    if a<=2:
        return 1
    return fibonacci(a-1)+fibonacci(a-2)

print(fibonacci(10))