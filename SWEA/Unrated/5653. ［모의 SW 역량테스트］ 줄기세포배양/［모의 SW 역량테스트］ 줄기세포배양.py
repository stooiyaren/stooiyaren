dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    start = [list(map(int,input().split())) for _ in range(N)]

    visited = [[False]*650 for _ in range(650)]

    wait = []
    cnt = 0

    for i in range(N):
        for j in range(M):
            if start[i][j] != 0:
                wait.append([-start[i][j],-start[i][j],i+300,j+300]) # [power, second, x,y]
                visited[i+300][j+300] = True
                cnt += 1
    
    for q in range(K): # K초 동안 반복
        wait.sort(key = lambda x:x[0])
        re = []
        for j in range(len(wait)):

            wait[j][1] += 1
            if wait[j][1] == 1:
                for k in range(4):
                    di = wait[j][2] + dx[k]
                    dj = wait[j][3] + dy[k]
                    if not visited[di][dj]:
                        re.append([wait[j][0],wait[j][0],di,dj])
                        cnt += 1
                        visited[di][dj] = True
            if wait[j][1] == -wait[j][0]:
                cnt -=1
            elif wait[j][1] < -wait[j][0]:
                re.append(wait[j])
        wait = re
    print(f'#{tc} {cnt}')