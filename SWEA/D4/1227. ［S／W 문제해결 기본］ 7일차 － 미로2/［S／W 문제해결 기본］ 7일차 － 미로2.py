di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(start, goal):
    maze[start[0]][start[1]] = 1
    q = deque()
    q.append(start)    
    ans = 0
    while q:
        start = q.popleft()       
        if start == goal:
            ans = 1
            return ans
        maze[start[0]][start[1]] = 1
        for i in range(4):
            dx = start[0]+di[i]
            dy = start[1]+dj[i]
            if 0 <= dx < 100 and 0 <= dy < 100 and (maze[dx][dy] == 0 or maze[dx][dy] == 3):
                q.append([dx,dy])
    return ans
    
from collections import deque

for tc in range(1,11):
    n = int(input())
    maze =[list(map(int,input())) for _ in range(100)]
    
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                S = [i,j]
            if maze[i][j] == 3:
                G = [i,j]
    print(f'#{tc}', bfs(S,G))