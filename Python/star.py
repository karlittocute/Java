# Кицела Каролина ИВТ 3 курс
# Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
# Напишите функцию, которая создаёт из этих ключей и значений словарь.
def dictionary(a,b):
    """
    Функция принимает 2 списка.
    Первый список это ключи, второй это значения.
    Создается словарь. Если ключу не хватило значения, то оно будет равно None.
    Лишние значения игнорируются.
    """
    res = dict()
    for i in range(len(a)):
        if i >= len(b):
            res[a[i]] = None
        else:
            res[a[i]] = b[i]
    return res



assert dictionary([],[]) == {}
assert dictionary([],[1]) == {}
assert dictionary(["aaa"],[]) == {"aaa":None}
assert dictionary(["aaa","bbb","ccc"],[1,2,3]) == {'ccc': 3, 'bbb': 2, 'aaa': 1}
assert dictionary(["aaa","bbb","ccc"],[1,2,3,6]) == {'ccc': 3, 'bbb': 2, 'aaa': 1}
assert dictionary(["aaa","bbb","ccc","www","ttt"],[1,2,3,6]) == {'ttt': None, 'www': 6, 'ccc': 3, 'aaa': 1, 'bbb': 2}