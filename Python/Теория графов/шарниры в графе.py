import sys

ribs = []                         # Описание ребер
v = 0                             # Кол-во вершин
adj_list = []                     # Список смежности
while True:
    ln = ''
    try:
        x,y= map(int, input().split())
    except:
        break
    s = [x,y]
    if max(s) > v: v = max(s)
    ribs.append(s)
sys.setrecursionlimit(10000)
print(ribs)
print(v)

vis = [False]*v                   # Список "посещаемости" вершин 



# Заполнение таблицы смежности
for i in range(v):
    adj_list.append([])
    for j in range(e):
        if ribs[j][0] == i:
            adj_list[i].append(ribs[j][1])
        elif ribs[j][1] == i:
            adj_list[i].append(ribs[j][0])

# Рекурсивная функция            
def search(v):
    vis[v] = True
    for i in adj_list[v]:
        if not vis[i]:
            search(i)

# Итерируемся по каждой вершине, и если мы ее не рассматривали,
# то прибавляем к k единицу и запускаем рекурсивную функцию  :)
for i in range(len(vis)):
    if not vis[i]:
        k += 1
        search(i)
print(k)
