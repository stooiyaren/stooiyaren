def danzo(n):
    while n >9:
        a = n%10
        b = n//10 %10
        if b>a:
            return 0
        n //= 10
    return 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Ai = list(map(int,input().split()))
    mx = 0

    for i in range(N-1):
        for j in range(i+1,N):
            num = Ai[i] * Ai[j]

            if danzo(num):
                if num > mx:
                    mx = num

    if mx == 0:
        mx = -1            
    print(f'#{tc}', mx)