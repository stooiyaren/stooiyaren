def dfs(x,y):
    global cnt

    if len(queenx) == N:
        cnt += 1
        return

    for i in range(y,N):
        for j in range(N):
            if check(j,i):
                queenx.append(j)
                queeny.append(i)
                queens.append([j,i])
                dfs(j,i)
                queenx.pop()
                queeny.pop()
                queens.pop()

def check(x,y):
    if y in queeny:
        return False
    if x in queenx:
        return False
    for k in queens:
        if abs(x - k[0]) == abs(y - k[1]):
            return False
    return True

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    chess = [[0]*N for _ in range(N)]
    cnt = 0
    queenx = []
    queeny = []
    queens = []
    for i in range(N):
        queenx.append(i)
        queeny.append(0)
        queens.append([i, 0])
        dfs(i,0)
        queenx.pop()
        queeny.pop()
        queens.pop()

    print(f'#{tc}', cnt)