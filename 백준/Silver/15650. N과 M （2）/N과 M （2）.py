def binary(i,cnt):
    global N, M
    if cnt > M:
        return
    
    if cnt == M:
        ans = []
        for p in range(N):
            if bit[p]:
                ans.append(num[p])
        print(*ans)
        return
    
    if i == N:
        return
    
    bit[i] = 1
    binary(i+1,cnt+1)
    bit[i] = 0
    binary(i+1,cnt)


N, M = map(int,input().split())

num = list(range(1,N+1))
bit = [0] *N
binary(0,0)