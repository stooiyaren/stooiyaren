def dfs(n,m):
    if len(ans) == m:
        print(' '.join(map(str,ans)))

    for i in range(1,n+1):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(i)
        dfs(n,m)
        visited[i] = False
        ans.pop()


    
N,M = map(int,input().split())

ans = []
visited = [0] * (N+1)
dfs(N,M)