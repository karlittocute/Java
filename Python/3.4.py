# Кицела К ИВТ 3 курс
# Реализовать два наиболее простых алгоритма шифрования для 
# шифрования/дешифрования текстовых файлов
def caesar(s):
    """
    Функция принимает строку и изменяет используя шифр Цезаря
    На вход должны подаваться только буквы английского алфавита
    Остальные символы неизменны 
    """
    res = ""
    for i in s:
        if ord(i) > 122 or ord(i) < 65 or (ord(i) > 90 and ord(i) < 97):
            res += i
        if ord(i)>=97 and ord(i)<=122:
            if ord(i)>=120:
                res +=(chr(ord(i)-23))

            else:
                res +=(chr(ord(i)+ 3))
        if ord(i)>=65 and ord(i)<=90:
            if ord(i)>=87:
                res +=(chr(ord(i)-23))

            else:
                res +=(chr(ord(i)+ 3))
    return res



def caesar_decode(s):
    """
    Функция принимает шифр Цезаря и возвращает расшифровку
    На вход должны подаваться только буквы английского алфавита
    Остальные символы неизменны 
    """
    res = ""
    for i in s:
        if ord(i) > 122 or ord(i) < 65 or (ord(i) > 90 and ord(i) < 97):
            res += i
        if ord(i)>=97 and ord(i)<=122:
            if ord(i) <= 99:
                res +=(chr(ord(i)+ 23))

            else:
                res +=(chr(ord(i)- 3))
        if ord(i)>=65 and ord(i)<=90:
            if ord(i) <= 67:
                res +=(chr(ord(i)+ 23))

            else:
                res +=(chr(ord(i)- 3))
    return res


assert caesar("abc") == "def"
assert caesar("xyz") == "abc"
assert caesar("ABC") == "DEF"
assert caesar("XYZ") == "ABC"
assert caesar("123") == "123"
assert caesar_decode("abc") == "xyz"
assert caesar_decode("def") == "abc"
assert caesar_decode("ABC") == "XYZ"
assert caesar_decode("DEF") == "ABC"
assert caesar_decode("123") == "123"
assert caesar_decode(caesar("xyzabcXYZABC123,]['=-")) == "xyzabcXYZABC123,]['=-"
