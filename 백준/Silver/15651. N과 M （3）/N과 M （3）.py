def c(i):
    global check
    if i == M:
        print(*ans)
        return
    
    for j in range(1,N+1):
        ans[i] = j
        c(i+1)
    
    

N, M = map(int,input().split())
# num = list(range(1,N+1))
ans = [0] * M
check = 0
c(0)