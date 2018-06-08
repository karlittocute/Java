#2.3
# Кицела Каролина ИВТ 3 курс 
# Вариант 22
# Дано множеств из 10 случайно полученных элементов.Найдите количество сочетаний
# с повторениями из n по k элементов

import math
def combination(inp_set,n,k):
  c_nk = math.factorial(n+k-1)/(math.factorial(k)*math.factorial(n-1))
  return c_nk