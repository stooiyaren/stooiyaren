def binary(num, last, hap):
    global cnt

    if hap == last:
        cnt += 1
        return
    
    if hap > last:
        return

    if num == N:
        return
    
    binary(num+1, last, hap + A[num])
    binary(num+1, last, hap)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())

    A = list(map(int,input().split()))
    cnt = 0
    binary(0,K,0)
    print(f'#{tc} {cnt}')