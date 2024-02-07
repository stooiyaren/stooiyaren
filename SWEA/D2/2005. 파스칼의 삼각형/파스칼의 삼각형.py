di = [-1, -1]
dj = [-1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * i for i in range(N+1)]

    for i in range(N+1):
        for j in range(i):
            if j == 0:
                matrix[i][j] = 1
            else:
                for k in range(2):
                    if 0 <= i+di[k] and 0 <= j+dj[k] < i-1:
                        matrix[i][j] += matrix[i+di[k]][j+dj[k]]

    print(f'#{tc}', end='')
    for i in range(N+1):
        for j in range(i):
            print(matrix[i][j], end = ' ')
        print()
