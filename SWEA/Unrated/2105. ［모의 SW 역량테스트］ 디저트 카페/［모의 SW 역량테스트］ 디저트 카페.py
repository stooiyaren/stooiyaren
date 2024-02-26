dx = [1,1,-1,-1]
dy = [1,-1,-1,1]


def dfs(x,y,direction,first,second,dessert):
    global N
    global ans

    if direction == 2:
        if not first or not second:
            return

        for p in range(1,first+1):
            ni = x + p * dx[2]
            nj = y + p * dy[2]

            if 0 <= ni < N and 0 <= nj < N and cafe[ni][nj] not in dessert:
               dessert += [cafe[ni][nj]]
            else:
                return
        for q in range(1,second): # 시작점은 이미 포함되어있으므로!)
            ri = ni + q * dx[3]
            rj = nj + q * dy[3]

            if 0 <= ri < N and 0 <= rj < N and cafe[ri][rj] not in dessert:
                dessert.append(cafe[ri][rj])
            else:
                return
        ans.append(len(dessert))

    elif direction == 0:
        di = x + dx[direction]
        dj = y + dy[direction]

        if 0 <= di < N and 0 <= dj < N and cafe[di][dj] not in dessert: # 새 좌표가 N 배열 안에 있을 때 디저트 무러 갑시다.
            dfs(di, dj, direction+1, first+1, second, dessert + [cafe[di][dj]])
            dfs(di, dj, direction, first+1, second, dessert + [cafe[di][dj]])

    elif direction == 1:
        di = x + dx[direction]
        dj = y + dy[direction]
        if 0 <= di < N and 0 <= dj < N and cafe[di][dj] not in dessert:
            dfs(di, dj, direction+1, first, second+1, dessert + [cafe[di][dj]])
            dfs(di, dj, direction, first, second+1, dessert + [cafe[di][dj]])



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cafe = [list(map(int,input().split())) for _ in range(N)]
    ans =[]
    for i in range(N-2): # 마름모를 그리는 특성상 아래 두칸이 존재해야함
        for j in range(1,N-1): # 마름모를 그리는 특성상 양 옆 두칸이 존재해야함
            dfs(i,j,0,0,0,[cafe[i][j]])
    if ans:
        print(f'#{tc} {max(ans)}')
    else:
        print(f'#{tc} -1')