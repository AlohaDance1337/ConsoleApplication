import math

def sum(a:int|float=None,b:int|float=None)->int|float:
    return a+b

def mul(a:int|float=None,b:int|float=None)->int|float:
    return a*b

def div(a:int|float=None,b:int|float=None)->int|float:
    try:
        return a/b
    except ZeroDivisionError:
        print("Делить на ноль нельзя")

def div_ex(a:int|float=None,b:int|float=None)->int|float:
    try:
        return a//b
    except ZeroDivisionError:
        print("Делить на ноль нельзя")

def dif(a:int|float=None,b:int|float=None)->int|float:
    return a-b

def sqrt(a:int|float=None)->int|float:
    return math.sqrt(a)

def exp(a:int|float=None)->int|float:
    return math.exp(a)

def factorial(a:int=None)->int|float:
    if a==1:
        return 1
    return factorial(a-1)*a

def log(a:int|float=None,b:int=None)->int|float:
    return math.log(b,a)
    
def ln(a:int|float=None)->float:
    return math.log(a,math.e)

def fibonacci(a:int=None)->int:
    if a<=2:
        return 1
    return fibonacci(a-1)+fibonacci(a-2)

def pow(a:int|float=None,b:int=None)->int|float:
        return math.pow(a,b)

