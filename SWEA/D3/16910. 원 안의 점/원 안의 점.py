T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    for i in range(N):
        for j in range(N):
            if i*i+j*j <= N*N:
                cnt += 1
    ans = 4*cnt - 4*(N+1) +1
    print(f'#{tc} {ans+8}')