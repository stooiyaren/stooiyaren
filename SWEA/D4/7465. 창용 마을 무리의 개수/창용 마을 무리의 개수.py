# 창용 마을 무리의 개수
# union find

def make_set(n):
    return list(range(n+1))

def find_set(x):
    if parent[x] == x:
        return x
    
    return find_set(parent[x])

def union(x,y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    
    if x < y:
        for i in range(N+1):
            if parent[i] == y:
                parent[i] = x
    else:
        for i in range(N+1):
            if parent[i] == x:
                parent[i] = y

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())

    parent = make_set(N)
    for _ in range(M):
        a, b = map(int,input().split())
        union(a,b)

    print(f'#{tc} {len(set(parent))-1}')