dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

from collections import deque

def tunnel(n):
    if n == 1:
        return [0,1,2,3]
    elif n == 2:
        return [0,1]
    elif n == 3:
        return [2,3]
    elif n == 4:
        return [0,3]
    elif n == 5:
        return [1,3]
    elif n == 6:
        return [1,2]
    elif n == 7:
        return [0,2]

def connect(start, end):
    if start == 0 and 1 in end:
        return True
    elif start == 1 and 0 in end:
        return True
    elif start == 2 and 3 in end:
        return True
    elif start == 3 and 2 in end:
        return True
    else:
        return False


def bfs(start):
    global L
    global ans
    q = deque()
    q.append(start)
    while q:
        start = q.popleft()

        if start[2] >= L:
            continue
        else:

            for i in tunnel(start[3]):
                di = start[0] + dx[i]
                dj = start[1] + dy[i]
                if 0<= di < N and 0 <= dj < M and sewer[di][dj] != 0:
                    if connect(i,tunnel(sewer[di][dj])):
                        q.append([di,dj,start[2]+1,sewer[di][dj]])
                        sewer[di][dj] = 0
                        ans += 1

T = int(input())
for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    sewer = [list(map(int,input().split())) for _ in range(N)]
    ans = 1
    start = [R,C,1,sewer[R][C]]
    sewer[R][C] = 0
    bfs(start)
    print(f'#{tc}', ans)