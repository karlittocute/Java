# Кицела К ИВТ 3 курс
# Провести рефакторинг калькулятора (использовать для ввода и вывода метод format()).

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
    return x**(1/y)

def calculate():
    print("Выберите операцию  +, -, *, /, ^, sqrt")
    k = input()

    if k not in ["+", "-", "*"," /", "^", "sqrt"]:
        print("Такой операции нет")
    else:
        x = float(input("Первое число "))
        y = float(input("Второе число "))
        if k == "+":
            print("{}".format(add(x,y)))
        elif k == '-':
            print("{}".format(substract(x,y)))
        elif k == '*':
            print("{}".format(multiply(x,y)))
        elif k == '^':
            print("{}".format(exponent(x,y)))
        elif k == 'sqrt':
            print("{}".format(root(x,y)))	
        elif k == '/':
            print("{}".format(divide(x,y)))



calculate()
        