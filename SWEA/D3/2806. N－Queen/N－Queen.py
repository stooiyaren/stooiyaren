# N-퀸 문제

# 중첩 함수(nested function):내부함수를 만들어서 간단하게 정리
def n_queen_solve(N):

    def dfs(depth):
        nonlocal count, visited, board
        if depth == N:
            count += 1
            return

        for col in range(N):
            if not visited[col] and check(depth, col):
                board[depth] = col
                visited[col] = True # 결정
                dfs(depth +1)
                visited[col] = False # 복구


    def check(row,col):
        for x in range(row):
            y = board[x]
            if abs(x-row) == abs(y-col):
                return False
        return True
    
    count = 0
    visited = [False] * N
    board = [-1]*N
    dfs(0)

    return count

T = int(input())
for tc in range(1,T+1):
	N = int(input()) # N 퀸의 N을 입력받아서
	print(f'#{tc} {n_queen_solve(N)}')