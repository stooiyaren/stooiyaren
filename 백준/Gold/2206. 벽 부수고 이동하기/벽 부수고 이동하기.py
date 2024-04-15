from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    global K

    visited[0][0] = [1] * (K+1)
    q = deque()
    q.append([0,0,K]) # [x좌표, y좌표, 현재 남은 벽부수는 횟수, 지나온 거리]

    while q:
        x,y, chance = q.popleft()

        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not jido[nx][ny]: # 길인 경우
                if visited[x][y][chance]+1 < visited[nx][ny][chance]:
                    q.append([nx,ny,chance])
                    visited[nx][ny][chance] = visited[x][y][chance]+1
            elif 0 <= nx < N and 0 <= ny < M and jido[nx][ny]: # 벽인경우
                if visited[x][y][chance]+1 < visited[nx][ny][chance-1]:
                    if chance: # 찬스가 남아있다면
                        q.append([nx,ny,chance-1]) # 찬스빼고 진격
                        visited[nx][ny][chance-1] = visited[x][y][chance]+1

N,M = map(int,input().split())
K = 1
jido = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[[float('inf')]*(K+1) for _ in range(M)] for _ in range(N)]
# start = 0,0, end = N-1 , M-1
bfs()

mn = float('inf')
mn = min(visited[N-1][M-1])
if mn == float('inf'):
    print(-1)
else:
    print(mn)