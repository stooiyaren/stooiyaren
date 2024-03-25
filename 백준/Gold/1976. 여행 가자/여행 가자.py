def find_set(x):
    if parent[x] ==x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]
def union(x,y):
    x = find_set(x)
    y = find_set(y)

    for i in range(N):
        if parent[i] == y:
            parent[i] = x

N = int(input())
M = int(input())

parent = list(range(N))

for i in range(N):
    doro = list(map(int,input().split()))

    for j in range(N):
        if doro[j]:
            union(i,j)

visit = list(map(int,input().split()))
trip = parent[visit[0]-1]
for i in visit:
    if parent[i-1] != trip:
        print('NO')
        break
else:
    print('YES')