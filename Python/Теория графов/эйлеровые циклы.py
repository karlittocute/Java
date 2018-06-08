n, m = map(int, input().split()) #количество вершин и ребер в графе
adj = [[] for i in range(n)] #список смежности
used = [False for i in range(m)] #массив для хранения информации о пройденных и не пройденных ребрах
ribs = []
res = []

#считываем граф, заданный списком ребер    
for i in range(m):
    v, w = map(int, input().split())
    v -= 1
    w -= 1
    x = [v,w]
    ribs.append(x)
    adj[v].append(w)
    adj[w].append(v) 

for i in range(n):
    if not len(adj[i])%2 == 0 or len(adj[i])<2:
        print("NONE")
        sys.exit()

def func(s,x):
    for i in adj[s]:   # Находим смежные вершины
        k = 0
        for j in range(m):    # находим нужное ребро 
            if (ribs[j] == [i,s] or ribs[j] == [s, i]) and not used[j]:
                used[j] = True
                res.insert(x,i)
                k +=1
                func(i,x+1)
                break
        if k==1 :
            break
res.append(0)
func(0,1)
for i in range(m):  # Ищем непройденные ребра
    if not used[i]:
        k = 0
        for j in res:   # ищем вершину из цикла которая принадлежит этому ребру
            k += 1
            if ribs[i][0] == j or ribs[i][1] == j:
                func(j,k)
                break

for i in range(len(res)):
    res[i] +=1
res.pop(len(res)-1)
print(' '.join(map(str, res)))
