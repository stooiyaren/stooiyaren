di = [-1,1,0,0]
dj = [0,0,-1,1]

def bfs(start, goal):
    maze[start[0]][start[1]] = 0
    q = deque()
    q.append(start)    
    while q:
        start = q.popleft()
        
        for i in range(4):
            dx = start[0]+di[i]
            dy = start[1]+dj[i]
            if [dx,dy] == goal:
                return start[2]+1
            if 0 <= dx < N and 0 <= dy < M and maze[dx][dy] == 1:
                q.append([dx,dy,start[2]+1])
                maze[dx][dy] = 0
    
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
maze =[deque(map(int,input().strip())) for _ in range(N)]

S = [0,0,1]
G = [N-1,M-1]
print(bfs(S,G))