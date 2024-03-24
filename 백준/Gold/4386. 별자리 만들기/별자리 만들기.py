def kru(edges):

    def find_set(x):
        if parent[x] ==x:
            return x

        parent[x] = find_set(parent[x])
        return parent[x]

    def union(x,y):
        x = find_set(x)
        y = find_set(y)

        if x == y:
            return
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    mst = 0
    parent = list(range(n))

    for l, i, j in edges:
        if find_set(i) != find_set(j):
            union(i,j)
            mst += l

    return mst

n = int(input())

starx = [0] * n
stary = [0] * n
for i in range(n):
    starx[i],stary[i] = map(float,input().split())
    
edges = []

for i in range(n-1):
    for j in range(i+1,n):
        L = ((starx[i]- starx[j])**2 + (stary[i]-stary[j])**2)**0.5
        edges.append((L,i,j))

edges.sort(key = lambda x : x[0])

print(round(kru(edges),2))