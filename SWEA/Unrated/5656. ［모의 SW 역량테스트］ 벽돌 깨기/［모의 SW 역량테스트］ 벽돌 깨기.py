dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    q = [start]
    while q:
        start = q.pop()
        for k in range(4):
            for l in range(start[2]):
                nx = start[0] + dx[k]*l
                ny = start[1] + dy[k]*l
                if 0<= nx < H and 0<= ny < W and blo[nx][ny] != 0:
                    q.append([nx,ny,blo[nx][ny]])
                    blo[nx][ny] = 0

def clean(n):

    for i in range(W):
        new = []
        for j in range(H):
            if n[j][i] != 0:
                new.append(n[j][i])

        new = (H - len(new))*[0] + new
        for j in range(H):
            n[j][i] = new[j]

def top(n):
    for i in range(H):
        if blo[i][n] != 0:
            return i
    return -1

from itertools import product
import copy

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int,input().split())
    block = [list(map(int, input().split())) for _ in range(H)]
    ans = []
    check = list(product(range(W), repeat = N))
    for game in check:
        blo = copy.deepcopy(block)
        for p in game:
            height = top(p)
            if height < 0:
                break
            power = blo[height][p]
            start = [height, p, power]
            bfs(start)
            clean(blo)

        cnt = 0
        for i in range(H):
            for j in range(W):
                if blo[i][j] != 0:
                    cnt += 1
        ans.append(cnt)
        if 0 in ans:
            break
    print(f'#{tc}', min(ans))