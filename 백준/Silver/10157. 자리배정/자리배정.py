dx = [0,1,0,-1]
dy = [1,0,-1,0]

C, R = map(int,input().split())
K = int(input())

if K > C*R:
    print(0)
else:
    snail = [[0]*R for _ in range(C)]
    x = 0
    y = 0
    d = 0

    for i in range(1,C*R+1):
        snail[x][y] = i
        if i == K:
            print(x+1,y+1)
            break

        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or C <= nx or ny < 0 or R <= ny or snail[nx][ny] != 0:
            if d == 3:
                d = 0
            else:
                d += 1
            x = x + dx[d]
            y = y + dy[d]

        else:
            x = nx
            y = ny