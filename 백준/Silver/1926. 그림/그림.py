from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    q = deque()
    q.append(start)
    paper[start[0]][start[1]] = 0
    mx = 1
    while q:
        start = q.popleft()
    
        for k in range(4):
            nx = start[0] + dx[k]
            ny = start[1] + dy[k]
            if 0<= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                q.append([nx,ny])
                paper[nx][ny] = 0
                mx += 1
    return mx

n, m = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
best = 0

for i in range(n):
    for j in range(m):
        
        if paper[i][j] == 1:
            cnt += 1
            b = bfs([i,j])
            if b > best:
                best = b
print(cnt)
print(best)