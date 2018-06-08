k, n = map(int,input().split())
m = {i for i in range(n)}
l = []



def func(k):
    print("k",k)
    print("ans",l)
    s = m.copy()
    for i in s:
        l.append(i)
        m.remove(i)
        if k > 1:
            func(k-1)
        else:
            print(l)
            l.pop()
            m.add(i)
            
        
func(k)
