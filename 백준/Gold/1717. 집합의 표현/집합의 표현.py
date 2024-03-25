import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    parent[x] = y

n, m = map(int,input().split())

parent = list(range(n+1))

for i in range(m):
    c, a, b = map(int,input().split())

    if c == 0:
        union(a,b)
    else:
        if find_set(a) == find_set(b):
            print('yes')
        else:
            print('no')