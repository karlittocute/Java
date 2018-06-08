# Кицела Каролина ИВТ 3 курс  
# Вариант 6
# №13
print "*"*45
print "*   A   *   B  *  C  *  (A&B<=>B&C)|(-C->A) *"
print "*"*45
for i in range(8):
  a = i//4
  b = (i%4)//2
  c = (i%4)%2
  if (c or a) or ((a and b) == (b and c )):
    res = "True"
  else:
    res = "False"
  print "*  ", a, "  *  ", b, " * ", c, " *        ",res, "        *" 
  print "*"*45
print ""
