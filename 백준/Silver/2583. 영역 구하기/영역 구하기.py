from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    cnt =1
    q = deque()
    q.append([i,j])
    paper[i][j] = 1
    while q:
        x, y = q.popleft()
        for n in range(4):
            nx = x+dx[n]
            ny = y+dy[n]
            if 0<=nx<M and 0<=ny<N and paper[nx][ny] ==0:
                cnt += 1
                paper[nx][ny] = 1
                q.append([nx,ny])
    return cnt


M, N, K = map(int,input().split())

paper = [[0]*N for _ in range(M)]

area = []

for i in range(K):
    y1,x1,y2,x2 = map(int,input().split())

    for x in range(x1,x2):
        for y in range(y1,y2):
            paper[x][y] = 1

for i in range(M):
    for j in range(N):
        if not paper[i][j]:
            area.append(bfs(i,j))

print(len(area))
area.sort()
print(*area)