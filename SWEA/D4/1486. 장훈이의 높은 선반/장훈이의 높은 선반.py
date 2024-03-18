def binary(i,k):
    global mn
    global B
    global N

    cnt = -B
    for j in range(i):
        if bit[j]:
            cnt += H[j]
    if cnt >= 0 and cnt >= mn:
        return
    
    if i == k:
        if cnt >= 0 and cnt < mn:
            mn = cnt
        return
        
    bit[i] = 0
    binary(i+1,k)
    bit[i] = 1
    binary(i+1,k)

T = int(input())
for tc in range(1,T+1):
    N,B = map(int,input().split())
    H = list(map(int,input().split()))
    H.sort()
    mn = sum(H) - B
    bit = [0]*N
    binary(0,N)
    print(f'#{tc} {mn}')