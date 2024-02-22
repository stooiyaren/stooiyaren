for tc in range(1, 11):
    N = int(input())
    cnt = 0

    board = [list(map(int, input().split())) for _ in range(N)]
    board = list(map(list,zip(*board)))

    for i in board:
        new = []
        for j in i:
            if j != 0:
                new.append(j)

        for p in range(len(new) - 1):
            if new[p] == 1 and new[p + 1] == 2:
                cnt += 1
    print(f'#{tc}', cnt)