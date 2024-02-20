T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    board = [['0']*(N+2)] + [(['0'] + list(map(str,input().split())) + ['0']) for _ in range(N)] + [['0'] * (N+2)]
    cnt = 0

    for i in range(len(board)):
        for j in range(len(board) - K -1):
            cross = []
            for k in range(K+2):
                cross.append(board[i][j+k])
            if cross == (['0'] + ['1']*K + ['0']):
                cnt += 1

    board = list(map(list,zip(*board)))

    for i in range(len(board)):
        for j in range(len(board) - K -1):
            cross = []
            for k in range(K+2):
                cross.append(board[i][j+k])
            if cross == (['0'] + ['1']*K + ['0']):
                cnt += 1

    print(f'#{tc}', cnt)
