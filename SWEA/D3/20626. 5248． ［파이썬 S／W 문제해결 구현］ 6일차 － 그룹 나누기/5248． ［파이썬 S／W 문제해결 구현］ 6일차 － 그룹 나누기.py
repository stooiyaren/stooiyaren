def make_set(n):
    return [i for i in range(n)]

def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])

def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return

    if x < y:
        parents[y] = x
        for i in range(N+1):
            if parents[i] == y:
                parents[i] = x
    else:
        parents[x] = y
        for i in range(N+1):
            if parents[i] == x:
                parents[i] = y

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    note = list(map(int,input().split()))
    parents = make_set(N+1)

    for i in range(M):
        union(note[i*2],note[i*2+1])
    print(f'#{tc} {len(set(parents))-1}')