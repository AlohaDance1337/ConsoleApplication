import math

def sum(a:int|float=None,b:int|float=None)->int|float:
    if type(a)==type(b)==int:
        return a+b
    else: raise TypeError("Тип переменной должен быть int")

def mul(a:int|float=None,b:int|float=None)->int|float:
    if type(a)==type(b)==int:
        return a*b
    else: raise TypeError("Тип переменной должен быть int")

def div(a:int|float=None,b:int|float=None)->int|float:
    if type(a)==type(b)==int:
        try:
            return a/b
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
    else: raise TypeError("Тип переменной должен быть int")

def div_ex(a:int|float=None,b:int|float=None)->int|float:
    if type(a)==type(b)==int:   
        try:
            return a//b
        except ZeroDivisionError:
            print("Делить на ноль нельзя")
    else: raise TypeError("Тип переменной должен быть int")    

def dif(a:int|float=None,b:int|float=None)->int|float:
    if type(a)==type(b)==int: 
        return a-b
    else: raise TypeError("Тип переменной должен быть int")  

def sqrt(a:int|float=None)->int|float:
    if type(a)==int or type(a)==float:
        return math.sqrt(a)
    else: raise TypeError("Тип переменной должен быть int") 

def exp(a:int|float=None)->int|float:
    if type(a)==int:
        return math.exp(a)
    else: raise TypeError("Тип переменной должен быть int") 

def module(a:int|float=None)->int|float:
    if type(a)==int:
        return abs(a)
    else: raise TypeError("Тип переменной должен быть int") 

def factorial(a:int=None)->int|float:
    if type(a)==int:
        if a==1:
            return 1
        return factorial(a-1)*a
    else: raise TypeError("Тип переменной должен быть int") 

def log(a:int|float=None,b:int=None)->int|float:
    if type(a)==type(b)==int:
        if(b!=0 and b>0) and (a!=1 and a>0):
            return math.log(b,a)
        else: raise ValueError("Основание логарифма не может быть равно нулю или число меньше нуля")
    
def ln(a:int|float=None)->float:
    if a!=0 and a>0:
        return math.log(a,math.e)
    else: raise ValueError("Основание логарифма не может быть равно нулю")

def fibonacci(a:int=None)->int:
    if type(a)==int:
        if a<=2:
            return 1
        return fibonacci(a-1)+fibonacci(a-2)
    else: raise TypeError("Тип переменной должен быть int")

def pow(a:int|float=None,b:int=None)->int|float:
    if type(a)==int:
        return math.pow(a,b)
    else: raise TypeError("Тип переменной должен быть int")

