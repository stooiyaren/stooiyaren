def seller(x,arg):
    global C
    global mx
    if x == len(arg):
        each = []
        for j in range(len(arg)):
            if bit[j]:
                each.append(arg[j])
        if sum(each) > C:
            return
        price = list(map(lambda x : x*x, each)) #path
        if sum(price) > mx:
            mx = sum(price)
            return
    else:
        bit[x] = 1
        seller(x+1, arg)
        bit[x] = 0
        seller(x+1, arg)


T = int(input())
for tc in range(1,T+1):
    N, M, C = map(int,input().split())
    hive = [list(map(int,input().split())) for _ in range(N)]
    harvest = [['']*N for _ in range(N)]
    best = 0

    for i in range(N):
        for j in range(N-M+1):
            honey = []
            for k in range(M):
                honey.append(hive[i][j+k])
            harvest[i][j] = honey

    for i in range(N):
        for j in range(N-M+1):
            bit = [0] * M
            mx = 0
            #path = []
            seller(0, harvest[i][j])
            harvest[i][j] = mx

    for i in range(N):
        for j in range(N-M+1):
            M1 = harvest[i][j]

            for p in range(N-1,-1,-1):
                if p < i:
                    break
                for q in range(N-M,-1,-1):
                    if (i < p) or (i == p and q > j+M):
                        M2 = harvest[p][q]
                        if best < M1 + M2:
                            best = M1+M2
    print(f'#{tc}', best)