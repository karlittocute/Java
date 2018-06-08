import sys 
a, b = map(str,input().split())   # А и В
ribs = []                         # Описание ребер
v = len(a)                        # Кол-во вершин
adj_list = []                     # Список смежности
sys.setrecursionlimit(10000)
s = []

vis = [False]*v                   # Список "посещаемости" вершин 



# Заполнение таблицы смежности
for i in range(v**2):
    print(i)
    n = []
    p = i
    for j in range(v):
        if p != 1:
            p = p//2
            n.append(p)
        else:
            n.append(p)
    s.append(n)
print(s)
# Рекурсивная функция            
def search(v):
    vis[v] = True
    for i in adj_list[v]:
        if not vis[i]:
            search(i)

# Итерируемся по каждой вершине, и если мы ее не рассматривали,
# то прибавляем к k единицу и запускаем рекурсивную функцию  :)
#for i in range(len(vis)):
 #   if not vis[i]:
#        k += 1
 #       search(i)
#print(k)
