
                                  
k = 0                             # Глубина
v, e = map(int,input().split())   # Кол-во вершин и ребер
ribs = []                         # Описание ребер
vis = [False]*v                   # Список "посещаемости" вершин                            # Кол-во компонент связаности 
adj_list = []                     # Список смежности
queue = [0]                       # Очередь
res = [0]+[-1]*(v-1)              # Результат

# ribs = {0:[0,1],1:[1,2],2:[2,0],3:[3,2],4:[4,3],5:[4,2],6:[5,4]}
# Ввод данных
for i in range(e):
    x,y = map(int,input().split())
    ribs.append([x,y])

# Заполнение таблицы смежности
for i in range(v):
    adj_list.append([])
    for j in range(e):
        if ribs[j][0] == i:
            adj_list[i].append(ribs[j][1])
        elif ribs[j][1] == i:
            adj_list[i].append(ribs[j][0])
            
def add_queue(k,*m):
    for i in m:
        if vis[i]== False:
            res[i] = k
            vis[i] = True
            queue.append(i)
   # queue.extend(m)
    queue.pop(0)

def rec(s, k):
    k = 1 +res[s]
    vis[s] = True
    add_queue( k, *adj_list[s])
    if queue and vis[queue[0]]:
        rec(queue[0], k)

rec(0,k)

print(' '.join(map(str, res)))
