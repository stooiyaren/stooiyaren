def sudoku(n):
    check = [1,2,3,4,5,6,7,8,9]

    for i in range(0,9,3):
        for j in range(0,9,3):
            square = []
            for p in range(3):
                for q in range(3):
                    square.append(n[p][q])
            if sorted(square) != check:
                return 0

    for i in n:
        if sorted(i) != check:
            return 0

    n = list(map(list,zip(*n)))

    for i in n:
        if sorted(i) != check:
            return 0

    return 1

T = int(input())
for tc in range(1,T+1):
    board = [list(map(int,input().split())) for _ in range(9)]

    print(f'#{tc}', sudoku(board))