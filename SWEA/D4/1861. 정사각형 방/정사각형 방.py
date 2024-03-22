# 정사각형 방

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append([x,y, square[x][y]])
    mn =square[x][y]
    square[x][y] = -1
    cnt = 1

    while q:
        x, y, height = q.popleft()

        for i in range(4):
            di = x + dx[i]
            dj = y + dy[i]

            if 0 <= di < N and 0 <= dj < N and square[di][dj] != -1:
                if abs(square[di][dj] - height) == 1:
                    q.append([di,dj,square[di][dj]])
                    cnt += 1

                    if square[di][dj] < mn:
                        mn = square[di][dj]

                    square[di][dj] = -1
    return cnt, mn


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    square = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    mini = 0

    for i in range(N):
        for j in range(N):
            if square[i][j] != -1:
                cal, num  = bfs(i,j)
                if  cal >= ans:

                    if cal == ans:
                        if mini > num:
                            mini = num
                    else:
                        ans = cal
                        mini = num
    print(f'#{tc} {mini} {ans}')