import sys
input = sys.stdin.readline

di = [1,1,1,0,-1,-1,-1,0]
dj = [1,0,-1,-1,-1,0,1,1]

while True:
    x, y = map(int,input().split())
    if x == y and x == 0:
        break
    mine = [list(input().strip()) for _ in range(x)]

    for i in range(x):
        for j in range(y):
            cnt = 0
            if mine[i][j] == '.':
                for k in range(8):
                    ni = i+di[k]
                    nj = j+dj[k]
                    if 0 <= ni < x and 0 <= nj < y and mine[ni][nj] == '*':
                        cnt += 1
                    mine[i][j] = cnt

    for i in range(x):
        for j in range(y):
            print(mine[i][j], end = '')
        print()