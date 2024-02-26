from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0,-1,1]

def bfs(start):
    q = deque()
    q.append(start)
    move = 0
    while q:
        start = q.popleft()

        for k in range(4):
            di = start[0] + dx[k]
            dj = start[1] + dy[k]

            if 0 <= di < N and 0 <= dj < N and rooms[di][dj] == (start[3] + 1):
                q.append([di,dj,start[2]+1,rooms[di][dj]])
                if start[2] +1 > move:
                         move = start[2] + 1
    return move
        

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    rooms = [list(map(int,input().split())) for _ in range(N)]
    best = 0
    ans = []
    
    for i in range(N):
        for j in range(N):
            n = bfs([i,j,1,rooms[i][j]])

            if n > best:
                best = n
                ans = [rooms[i][j]]
            elif n == best:
                ans.append(rooms[i][j])
    print(f'#{tc}', min(ans), best)