import sys
from collections import deque
input = sys.stdin.readline

def bfs(num):
    q = deque()
    q.append(num)
    visited[num] = 1
    cnt = 0
    while q:
        start = q.popleft()

        for i in computer[start]:
            if not visited[i]:
                q.append(i)
                visited[i]= 1
                cnt += 1
    return cnt

N = int(input())
computer = [[] for _ in range(N+1)]

route = int(input())
for r in range(route):
    s, e = map(int,input().split())
    computer[s].append(e)
    computer[e].append(s)

visited = [0]*(N+1)
if computer[1]:
    print(bfs(1))
else:
    print(0)
