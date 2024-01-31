T = int(input())
for t in range(1,T+1):
    N,K = map(int,input().split())
    matrix = [[0]*(N+2)]*(N+2)
    answer = [0] + [1]*K +[0]
    for i in range(1,N+1):
        n = list(map(int,input().split()))
        matrix[i] = [0]+ n +[0]
    cnt = 0
    for i in range(N-K+1):
        for j in range(N+2):
            lst = []
            for k in range(K+2):
                lst.append(matrix[i+k][j])
            if lst == answer:
                cnt +=1
    for i in range(N+2):
        for j in range(N-K+1):
            lst = []
            for k in range(K+2):
                lst.append(matrix[i][j+k])
            if lst == answer:
                cnt +=1
    print(f'#{t} {cnt}')