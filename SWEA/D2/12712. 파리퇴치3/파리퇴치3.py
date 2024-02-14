dx = [-1,0,0,1]
dy = [0,-1,1,0]

rx = [1,1,-1,-1]
ry = [-1,1,-1,1]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    best = 0
    for i in range(N):
        for j in range(N):
            
            pfly = matrix[i][j]
            xfly = matrix[i][j]
            for k in range(1,M):
                for l in range(4):
                    
                    nx = i + dx[l]*k
                    ny = j + dy[l]*k
                    
                    tx = i + rx[l]*k
                    ty = j + ry[l]*k
                    
                    if 0 <= nx < N and 0 <= ny < N:
                        pfly += matrix[nx][ny]
                    if 0 <= tx < N and 0 <= ty < N:
                        xfly += matrix[tx][ty]
            
            if best < max(pfly, xfly):
                best = max(pfly, xfly)
    print(f'#{tc}', best)