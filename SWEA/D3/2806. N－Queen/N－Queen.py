dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, chess):
    global cnt
    if x == N:
        cnt += 1
        return
    for y in range(N):
        if chess[x][y] == 0:
            chess_copy = [row[:] for row in chess]
            bfs(x, y, chess_copy)
            dfs(x + 1, chess_copy)

def bfs(x, y, chess):
    chess[x][y] = 1
    for k in range(8):
        l = 1
        nx = x + dx[k] * l
        ny = y + dy[k] * l
        while 0 <= nx < N and 0 <= ny < N:
            chess[nx][ny] = 1
            l += 1
            nx = x + dx[k] * l
            ny = y + dy[k] * l

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        dfs(0, chess)
        bfs(0, i, chess)
    
    print(f'#{tc}', cnt)