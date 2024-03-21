from collections import deque
import heapq

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(road):
    global N

    visited = [[float('inf')]*N for _ in range(N)]
    q = deque()
    q.append([0,0])
    visited[0][0] = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            di = x + dx[i]
            dj = y + dy[i]
            if 0 <= di < N and 0 <= dj < N:
                if visited[x][y] + road[di][dj] < visited[di][dj]:
                    visited[di][dj] = visited[x][y] + road[di][dj]
                    q.append([di,dj])
    return visited[N-1][N-1]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    road = [list(map(int,input().rstrip())) for _ in range(N)]

    print(f'#{tc} {bfs(road)}')