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
    parent = list(range(V+1))

    for l, i, j in edges:
        if find_set(i) != find_set(j):
            union(i,j)
            mst += l

    return mst

V, E = map(int,input().split())

edges = []

for i in range(E):
    A, B, C = map(int,input().split())

    edges.append((C,A,B))

edges.sort(key = lambda x : x[0])

print(kru(edges))
