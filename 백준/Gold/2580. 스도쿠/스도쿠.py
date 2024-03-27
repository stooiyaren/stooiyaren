import sys
input = sys.stdin.readline
# 각 0에 1-9까지 넣으면서 스도쿠 판별에서 걸러지면 prunning
def puzzle(i):
    global cnt, zero
    if cnt: # 답을 이미 구했으면 뒤도 안돌아보고 종료
        return

    if i == len(zero):
        # 끝까지 살아남는 친구가 정답
        for p in sdoku:
            print(*p)
        print()
        # 한개만 나오면 바로 종료
        cnt = 1
        return

    x,y = zero[i]
    for j in range(1,10):
        if check(x,y,j):
            sdoku[x][y] = j
            puzzle(i+1)
            sdoku[x][y] = 0


# 스도쿠 판별 함수를 만들고
def check(x,y,z): # z를 넣었을 시 확인해봅시다
    # x 줄 확인
    for i in range(9):
        if sdoku[x][i] == z:
            return False
    # y 줄 확인
    for i in range(9):
        if sdoku[i][y] == z:
            return False
    # 사각형 확인
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            if sdoku[i][j] == z:
                return False
    return True # 모든걸 다 통과하면 safe

sdoku = [list(map(int,input().split())) for _ in range(9)]
    
# 0인 부분의 좌표를 리스트로 만들고
zero = []
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            zero.append((i,j))
cnt = 0
puzzle(0)