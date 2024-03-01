def secure(x,y):
    global N
    global K
    global best

    for k in range(1, K+1):
        cnt = 0
        for i in range(x-k+1,x+k):
            for j in range(y-k+1,y+k):
                if 0 <= i < N and 0 <= j < N:
                    if k-1 >= (abs(x-i) + abs(y-j)):
                        if village[i][j] == 1:
                            cnt += 1
        if cnt * M >= k**2 + (k-1)**2:
            if best < cnt:
                best = cnt

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    village = [list(map(int,input().split())) for _ in range(N)]

    home = 0
    for i in village:
        home += sum(i)

    K = 1
    while home * M > K**2 + (K-1)**2:
        K += 1
    K -= 1
        
    best = 0
    for i in range(N):
        for j in range(N):
            secure(i,j)

    print(f'#{tc}', best)