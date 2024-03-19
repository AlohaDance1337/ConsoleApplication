from core.functions import *

lst = ["+", "-", "/", "*", "//", "sqrt", "e^x", "n!", "log", "ln", "Fib", "x^a"]
while True:
    print(f"Выберите, то что хотите выполнить: {', '.join(lst)}",)
    action = input()
    match action.split():
        case ["+"]:
            print(f"Вы выбрали сложение")
            digit1=float(input("Введите первое число: "))
            digit2=float(input("Введите второе число: "))
            value = sum(digit1,digit2)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["-"]:
            print(f"Вы выбрали вычитание")
            digit1=float(input("Введите первое число: "))
            digit2=float(input("Введите второе число: "))
            value = dif(digit1,digit2)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["*"]:
            print(f"Вы выбрали умножение")
            digit1=float(input("Введите первое число: "))
            digit2=float(input("Введите второе число: "))
            value = mul(digit1,digit2)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["/"]:
            print(f"Вы выбрали деление")
            digit1=float(input("Введите первое число: "))
            digit2=float(input("Введите второе число: "))
            value = div(digit1,digit2)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["//"]:
            print("Вы выбрали деление нацело")
            digit1=float(input("Введите первое число: "))
            digit2=float(input("Введите второе число: "))
            value = div_ex(digit1,digit2)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["sqrt"]:
            print("Вы выбрали sqrt")
            digit1=float(input("Введите число: "))
            value = sqrt(digit1)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["e^x"]:
            print("Вы выбрали e^x")
            digit1=float(input("Введите число: "))
            value = exp(digit1)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["n!"]:
            print(f"Вы выбрали ")
            digit1=int(input("Введите число: "))
            value = factorial(digit1)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["log"]:
            print(f"Вы выбрали log")
            digit1=float(input("Введите число: "))
            digit2=float(input("Введите основание:"))
            value = log(digit1,digit2)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["ln"]:
            print(f"Вы выбрали ln")
            digit1=float(input("Введите число: "))
            value = ln(digit1)
        case ["Fib"]:
            print(f"Вы выбрали Fib")
            digit1=int(input("Введите число: "))
            value = fibonacci(digit1)
            print(f"Значение полученное при выполненни программы: {value}")
        case ["x^a"]:
            print(f"Вы выбрали x^a")
            digit1=float(input("Введите число: "))
            digit2=float(input("Введите степень: "))
            value = pow(digit1,digit2)
            print(f"Значение полученное при выполненни программы: {value}")