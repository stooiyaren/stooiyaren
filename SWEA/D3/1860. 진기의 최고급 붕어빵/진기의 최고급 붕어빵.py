import math

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int,input().split())
    n = list(map(int,input().split()))
    time = [0]*11112
    ans = 0
    for i in range(N):
        time[n[i]] += 1

    for j in range(1,math.ceil(max(n)/M)+1):
        if sum(time[:j*M]) > K*(j-1):
            print(f'#{tc}', 'Impossible')
            ans = 1
            break
    if not ans:
        print(f'#{tc}', 'Possible')