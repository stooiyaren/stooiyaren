di = [0,0,1,-1]
dj = [-1,1,0,0]
ai = [1,1,-1,-1]
aj = [1,-1,1,-1]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    mx_fly = 0


    for i in range(N):
        for j in range(N):
            pfly = matrix[i][j]
            xfly = matrix[i][j]

            for p in range(4):
                for q in range(1,M):
                    pi = i +di[p]*q
                    pj = j +dj[p]*q
                    xi = i +ai[p]*q
                    xj = j +aj[p]*q

                    if 0<= pi and pi < N and 0 <= pj and pj < N:
                        pfly += matrix[pi][pj]

                    if 0 <= xi and xi <N and 0 <= xj and xj < N:
                        xfly += matrix[xi][xj]
                        
            if mx_fly < max(pfly, xfly):
                mx_fly = max(pfly, xfly)
    print(f'#{tc} {mx_fly}')