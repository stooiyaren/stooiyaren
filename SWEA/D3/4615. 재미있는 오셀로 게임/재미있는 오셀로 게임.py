dx = [-1, -1, -1, 0,0,1,1,1]
dy = [-1, 0, 1, 1,-1,0,1,-1]

def reversi(x, y, color,othello):
    othello[x-1][y-1] = color
    start = [x-1,y-1]
    if color == 1:
        change = []
        for i in range(8):
            nx, ny = start[0] + dx[i], start[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and othello[nx][ny] == 2:
                change.append([nx,ny,i])
        for j in change:
            stack = []
            begin = [j[0],j[1]]
            while True:
                stack.append(begin)
                nx, ny = begin[0] + dx[j[2]], begin[1] + dy[j[2]]
                if 0 <= nx < N and 0 <= ny < N and othello[nx][ny] == 1:
                    for k in stack:
                        othello[k[0]][k[1]] = 1
                    break
                elif 0 <= nx < N and 0 <= ny < N and othello[nx][ny] == 2:
                    begin = [nx,ny]
                else:
                    break
    elif color == 2:
        change = []
        for i in range(8):
            nx, ny = start[0] + dx[i], start[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N and othello[nx][ny] == 1:
                change.append([nx,ny,i])
        for j in change:
            stack = []
            begin = [j[0],j[1]]
            while True:
                stack.append(begin)
                nx, ny = begin[0] + dx[j[2]], begin[1] + dy[j[2]]
                if 0 <= nx < N and 0 <= ny < N and othello[nx][ny] == 2:
                    for k in stack:
                        othello[k[0]][k[1]] = 2
                    break
                elif 0 <= nx < N and 0 <= ny < N and othello[nx][ny] == 1:
                    begin = [nx,ny]
                else:
                    break
T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    othello = [[0]*N for _ in range(N)]
    othello[N//2][N//2] = 2
    othello[N//2-1][N//2-1] = 2
    othello[N//2-1][N//2] = 1
    othello[N//2][N//2-1] = 1
    
    for i in range(M):
        x, y, color = map(int,input().split())
        reversi(x,y, color,othello)
       
    black = 0
    white = 0    
    for a in othello:
        black += a.count(1)
        white += a.count(2)
    
    print(f'#{tc} {black} {white}')