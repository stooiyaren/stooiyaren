T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    a = len(A)
    ans = 0
    
    for i in range(1<<a):
        cnt = 0
        for j in range(a):
            if i &(1<<j):
                cnt += A[j]
        if cnt == K:
            ans += 1
    print(f'#{tc} {ans}')