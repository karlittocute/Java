# Кицела Каролина ИВТ 3 курс  
# Вариант 6
# Конъюкция
# Штрих Шеффера

a =  1
b = 0
print "*"*33 
print "*   A   *   B  * A & B *  A | B *" 
print "*"*33


for i in range(4):
  a = i // 2
  b = i % 2
  if a and b:
   k = "True"
  else:
   k = "False"
  if not (a and b):
   sh = "True"
  else:
   sh = "False"
  print "*  ", a, "  *  ", b, " *", k, "* ", sh, " *  "
  print "*"*33

print ""