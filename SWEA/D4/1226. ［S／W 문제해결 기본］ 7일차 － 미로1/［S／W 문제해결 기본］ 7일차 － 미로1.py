from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start,end):
    q = deque()
    q.append(start)
    maze[start[0]][start[1]] = 1
    ans = 0
    while q:
        start = q.popleft()
        
        for i in range(4):
            nx = start[0] + dx[i]
            ny = start[1] + dy[i]
            if maze[nx][ny] == 3:
                ans = 1
                return ans
            if 0<= nx<16 and 0<= ny <16 and maze[nx][ny] == 0:
                q.append([nx,ny])
                maze[nx][ny] = 1
    return ans   

for tc in range(1,11):
    T = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i,j]
            if maze[i][j] == 3:
                end = [i,j]
    
    print(f'#{T}', bfs(start,end))