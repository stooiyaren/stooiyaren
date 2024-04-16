import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
        global zero
        
        nxt = []
        for x,y in start:
                for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and storage[nx][ny] == 0:
                                nxt.append((nx,ny))
                                storage[nx][ny] = 1
                                zero -= 1

        return nxt

M,N = map(int,input().split())
storage = [list(map(int,input().split())) for _ in range(N)]

day = 0
start = []
zero = 0

for i in range(N):
        for j in range(M):
                if storage[i][j] == 1:
                        start.append((i,j))
                elif storage[i][j] == 0:
                        zero += 1

if not zero:
        print(0)
else:
        while start:
                start = bfs(start)
                day += 1

        if zero:
                print(-1)
        else:
                print(day-1)