import sys
input = sys.stdin.readline

di = [1,1,1,0,-1,-1,-1,0]
dj = [1,0,-1,-1,-1,0,1,1]

N = int(input())
mine = [list(input().strip()) for _ in range(N)]
check = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if mine[i][j] != '.':
            mine[i][j] = int(mine[i][j])
            check[i][j] = '*'
for i in range(N):
    for j in range(N):
        cnt = 0
        if mine[i][j] == '.':
            for k in range(8):
                ni = i+di[k]
                nj = j+dj[k]
                if 0 <= ni < N and 0 <= nj < N and mine[ni][nj] != '.':
                    cnt += mine[ni][nj]
                if cnt >=10:
                    check[i][j] = 'M'
                else:
                    check[i][j] = cnt 
            
for i in range(N):
    for j in range(N):
        print(check[i][j], end = '')
    print()
