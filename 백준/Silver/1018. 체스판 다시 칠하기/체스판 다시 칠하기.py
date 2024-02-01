M, N = map(int,input().split())
matrix = [list(str(input())) for _ in range(M)]
chess = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]
board = [['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],['W','B','W','B','W','B','W','B']]
fix = 65
for i in range(M-8+1):
    for j in range(N-8+1):
        wrong = 0
        wrong1 = 0
        for p in range(8):
            for q in range(8):
                if chess[p][q] != matrix[i+p][j+q]:
                    wrong += 1
                if board[p][q] != matrix[i+p][j+q]:
                    wrong1 += 1
        if min(wrong,wrong1) < fix:
              fix = min(wrong,wrong1)
print(fix)