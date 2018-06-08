v, e = map(int,input().split())   # Кол-во вершин и ребер
ribs = []                         # Описание ребер
vis = [False]*v                   # Список "посещаемости" вершин 
k = 0                             # Кол-во компонент связаности 
adj_list = []                     # Список смежности

# Ввод данных
for i in range(e):
    x,y = map(int,input().split())
    ribs.append([(x-1),(y-1)])

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
