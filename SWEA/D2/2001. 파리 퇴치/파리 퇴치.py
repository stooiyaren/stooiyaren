T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    best = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0

            for p in range(M):
                for q in range(M):
                    fly += matrix[i+p][j+q]
            if fly > best:
                best = fly
    print(f'#{tc} {best}')