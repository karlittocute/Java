# Кицела К ИВТ 3 курс
# Факториал

def fact(x):
    """
    Функция вычисляет факториал.
    Принимает один аргумент типа int, которое должно быть положительным
    """
    if type(x) != int:
        print("Неверный тип данных")
        return None
    if x < 0:
        print("Число отрицательное")
        return None
    if(x == 0 or x == 1):
        return 1		
    else:
        return fact(x-1) * x
  
assert fact(0) == 1
assert fact(1) == 1
assert fact(-1) == None
assert fact(0.5) == None
assert fact("asdasda") == None
assert fact(3) == 6
assert fact(5) == 120
