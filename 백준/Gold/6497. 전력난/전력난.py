import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def kru(edges):

    def find_set(x):
        if parent[x] == x:
            return x
        
        parent[x] = find_set(parent[x])
        return parent[x]
    
    def union(x,y):
        x = find_set(x)
        y = find_set(y)

        parent[x] = y
    
    mst = 0
    parent = list(range(m))

    for dist, start, end in edges:
        if find_set(start) != find_set(end): # 부모(대표자)가 다르다면
            union(start,end) # 합칩시다.
            mst += dist

    return mst

while True:
    m, n = map(int,input().split())
    if m == n == 0:
        break
    edges = []
    cnt = 0

    for i in range(n):
        x, y, z = map(int,input().split())
        edges.append((z,x,y)) #(거리, 시작, 종료)
        cnt += z
        
    edges.sort(key = lambda x: x[0])
    ans = cnt - kru(edges)
    print(ans)