for t in range(1, 11):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    col = matrix[99].index(2)
    row = 99

    while row > 0:
        if col > 0 and matrix[row][col - 1] == 1:
            while col > 0 and matrix[row][col - 1] == 1:
                col -= 1
            row -= 1
        elif col < 99 and matrix[row][col + 1] == 1:
            while col < 99 and matrix[row][col + 1] == 1:
                col += 1
            row -= 1
        else:
            row -= 1

    print(f'#{t} {col}')
