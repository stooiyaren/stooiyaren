import copy
import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,0,0,-1,1]
dy = [0,0,-1,1,0,0]
dz = [-1,1,0,0,0,0]

def check(box):
    cc = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 1:
                    q.append((i,j,k,0))
                if box[i][j][k] == 0:
                    cc += 1
    return cc

def bfs(z,x,y,timer):
    global zcnt
    global second

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0<= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
            box[nz][nx][ny] = 1
            zcnt -= 1
            q.append((nz,nx,ny,timer+1))
            if timer+1 > second:
                second = timer+1

M,N,H = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
second = 0
zcnt = check(box)
while q:
    if zcnt == 0:
        break
    i,j,k,timer = q.popleft()
    bfs(i,j,k,timer)

if zcnt:
    print(-1)
else:
    print(second)