T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int,input())) for _ in range(N)]
    cnt = 0
    a = N //2
    
    for i in range(N):
        cnt += sum(field[i])

    for i in range(N):
        for j in range(abs(a-i)):
            cnt -= field[i][j]
            cnt -= field[i][-(j+1)]

    print(f'#{tc}', cnt)