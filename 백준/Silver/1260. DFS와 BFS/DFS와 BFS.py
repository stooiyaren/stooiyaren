import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    ans = []
    while q:
        start = q.popleft()
        ans.append(start)
        for i in route[start]:
            if bisited[i]:
                continue
            else:
                bisited[i] = 1
                q.append(i)
    return ans
    
def dfs(n):
    for i in route[n]:
        if visited[i]:
            visited[i] = 0
            ddffss.append(i)
            dfs(i)
    else:
        return 

N,M,V = map(int,input().split())
route = [0]*(N+1)
visited = [1]*(N+1)
bisited = [0]*(N+1)
for i in range(M):
    one, two = map(int,input().split())
    if route[one]:
        route[one].append(two)
    else:
        route[one] = [two]
    if route[two]:
        route[two].append(one)
    else:
        route[two] = [one]
for i in range(1,len(route)):
    if route[i]:
        route[i].sort()
if route[V]:
    ddffss = [V]
    bisited[V] = 1
    visited[V] = 0
    dfs(V)
    print(*ddffss)
    print(' '.join(map(str,bfs(V))))
else:
    print(V)
    print(V)