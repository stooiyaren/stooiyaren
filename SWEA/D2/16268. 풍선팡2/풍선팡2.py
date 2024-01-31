T = int(input())
for t in range(1, T+1):
    N,M = map(int,input().split())
    matrix =[[0]*(M+2)]*(N+2)
    for i in range(1,N+1):
        n = list(map(int,input().split()))
        matrix[i] = [0] + n + [0]
    pollen = 0
    best = 0

    for i in range(1,N):
        for j in range(1,M):
            pollen = matrix[i][j] + matrix[i-1][j] + matrix[i+1][j] + matrix[i][j-1] + matrix[i][j+1]
            if pollen > best:
                best = pollen
    print(f'#{t} {best}')