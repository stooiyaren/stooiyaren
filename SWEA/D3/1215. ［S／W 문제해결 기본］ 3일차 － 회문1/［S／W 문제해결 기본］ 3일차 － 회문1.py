for tc in range(1,11):
    N = int(input())
    board = [input() for _ in range(8)]
    cnt = 0
    
    for i in range(8):
        for j in range(9-N):
            palin = []
            for k in range(N):
                palin.append(board[i][j+k])
            if palin == palin[::-1]:
                cnt += 1
                
    board = [list(i) for i in zip(*board)]
    for i in range(8):
        for j in range(9-N):
            palin = []
            for k in range(N):
                palin.append(board[i][j+k])
            if palin == palin[::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')