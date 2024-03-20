def dfs(n,probability):
    global N
    global mx
    if probability <= mx:
        return

    if n == N:
        if mx < probability:
            mx = probability
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            dfs(n+1,probability*work[n][i]/100)
            visited[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    work  = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N
    mx = 0
    dfs(0,100)
    print(f'#{tc} {mx:.6f}')