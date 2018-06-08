import queue

n, m = map(int, input().split()) #количество вершин и ребер в графе
adj = [[] for i in range(n)] #список смежности
used = [False for i in range(n)] #массив для хранения информации о пройденных и не пройденных вершинах
q = queue.Queue() #очередь для добавления вершин при обходе в ширину
res = [-1 for i in range(n)]
res[0]=0
#считываем граф, заданный списком ребер    
for i in range(m):
    v, w = map(int, input().split())
    adj[v].append(w)
    adj[w].append(v)
   
def bfs(v): #процедура обхода в ширину
    if used[v]: #если вершина является пройденной, то не производим из нее вызов процедуры
        return
    q.put(v); #начинаем обход из вершины v
    used[v] = True #начинаем обход из вершины v
    while(not q.empty()): #пока в очереди есть хотя бы одна вершина
        v = q.get() #извлекаем вершину из очереди
        for w in adj[v]: #запускаем обход из всех вершин, смежных с вершиной v
            if not used[w]: #если вершина уже была посещена, то пропускаем ее
                q.put(w) #добавляем вершину в очередь обхода
                res[w] = res[v]+1
                used[w] = True #помечаем вершину как пройденную
       
#def run():
#    for v in range(n):
#        bfs(v)

#run()
bfs(0)
print(' '.join(map(str, res)))
