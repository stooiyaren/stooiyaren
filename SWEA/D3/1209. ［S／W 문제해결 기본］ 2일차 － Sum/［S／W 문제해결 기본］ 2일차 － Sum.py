for t in range(10):
    T = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
 
    cnt = 0
    for i in range(100):
        cnt += matrix[i][i]
    cross1 = cnt
 
    cnt = 0
    for i in range(100):
        cnt += matrix[i][99-i] # 100*100 matrix 의 최댓값은 99
    cross2 = cnt
 
    cnt = 0
    coloum_best = 0
    for i in range(100):
        cnt = sum(matrix[i])
        if cnt > coloum_best:
            coloum_best = cnt
 
    row_best =0
    for i in range(100):
        cnt = 0
        for j in range(100):
            cnt += matrix[j][i]
        if cnt > row_best:
            row_best = cnt
 
    print(f'#{T}', max(cross1, cross2, coloum_best, row_best))