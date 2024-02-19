dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    q = [start]
    field[start[0]][start[1]] = 0
    while q:
        start = q.pop()
        
        for k in range(4):
            nx = start[0] + dx[k]
            ny = start[1] + dy[k]

            if 0 <= nx < M and 0 <= ny < N and field[nx][ny] == 1:
                q.append([nx,ny])
                field[nx][ny] = 0

T = int(input())
for tc in range(T):
    M, N, K = map(int,input().split())

    field = [[0]*N for _ in range(M)]

    for i in range(K):
        x,y = map(int,input().split())
        field[x][y] = 1

    worm = 0

    for i in range(M):
        for j in range(N):

            if field[i][j] == 1:
                bfs([i,j])
                worm += 1

    print(worm)