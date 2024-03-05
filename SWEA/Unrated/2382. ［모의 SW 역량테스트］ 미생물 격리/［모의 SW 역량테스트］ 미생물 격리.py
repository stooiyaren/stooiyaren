dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

def pesticide(n):
    if n[0] == 0 or n[0] == N-1 or n[1] == 0 or n[1] == N-1:
        if n[3]%2 == 0:
            return [n[0], n[1], n[2]//2, n[3] - 1]
        else:
            return [n[0], n[1], n[2]//2, n[3] + 1]
    return n

def mna(n):
    field = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(len(n)):
        field[n[i][0]][n[i][1]].append([n[i][2],n[i][3]])

    for i in range(N):
        for j in range(N):
            if len(field[i][j]) > 1:
                field[i][j].sort(key = lambda x: x[0], reverse = True)
                cnt = 0
                for p in field[i][j]:
                    cnt += p[0]
                field[i][j] = [[cnt,field[i][j][0][1]]]


    ng = []
    for i in range(N):
        for j in range(N):
            if len(field[i][j]):
                ng.append([i,j,field[i][j][0][0],field[i][j][0][1]])
    return ng


T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    germ = [0] * K
    for i in range(K):
        x,y,g,d = map(int,input().split())
        germ[i] = [x,y,g,d]

# ----------------------- setting ----------------

    for _ in range(M):
        for j in range(len(germ)):

            germ[j] = [germ[j][0]+dx[germ[j][3]], germ[j][1]+dy[germ[j][3]], germ[j][2], germ[j][3]]

            germ[j] = pesticide(germ[j])

        germ = mna(germ)

    cnt = 0
    for i in germ:
        cnt += i[2]
    print(f'#{tc}', cnt)