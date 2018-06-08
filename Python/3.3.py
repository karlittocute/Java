# Кицела Каролина ИВТ 3 курс
# Реализуйте основу для работы калькулятора (несколько функций для 
# вычисления основных операций).
def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y
  
def  divide(x,y):
    if y == 0:
        print("Деление на 0")
        return None
    return x/y

def exponent(x,y):
    return x**y

def root(x,y):
    if x < 0:
        print("У отрицательного числа нет корня")
        return None
    return x**(divide(1,y))
    
   
assert add(5,8) == 13
assert add(5,-8) == -3
assert substract(5,8) == -3
assert substract(8,5) == 3
assert multiply(5,8) == 40
assert multiply(5,0) == 0
assert multiply(5,-2) == -10
assert divide(5,0) == None
assert divide(25,5) == 5
assert divide(25,-5) == -5
assert exponent(25,0) == 1
assert exponent(25,-1) == 0.04
assert root(25,2) == 5
assert root(25,-2) == 0.2
assert root(0,2) == 0