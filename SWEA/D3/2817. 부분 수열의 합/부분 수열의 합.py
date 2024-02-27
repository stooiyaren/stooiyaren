def f(x):
    global N
    global K
    global ans
    if x == N:
        cnt = 0
        for j in range(N):
            if bit[j]:
                cnt += n[j]
        if cnt == K:
            ans += 1
            return

    else:
        bit[x] = 1
        f(x+1)
        bit[x] = 0
        f(x+1)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    ans = 0
    n = list(map(int,input().split()))
    bit = [0] * N
    f(0)
    print(f'#{tc}', ans)