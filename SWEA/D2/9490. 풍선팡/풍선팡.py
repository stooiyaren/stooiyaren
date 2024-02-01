T = int(input())
for t in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    di = [-1,0,0,1]
    dj = [0,-1,1,0]
    pollen = 0
    best = 0
    for i in range(N):
        for j in range(M):
            pollen = matrix[i][j]
            if pollen ==0:
                continue
            else:
                for p in range(1,pollen+1):
                    for q in range(4):
                        if 0<= (i+di[q]*p) < N and 0<= (j+dj[q]*p) < M:
                            pollen += matrix[i+di[q]*p][j+dj[q]*p]
                    if pollen > best:
                        best = pollen
    print(f'#{t} {best}')