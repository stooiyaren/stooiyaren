from collections import deque

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

# 장애물 1,2,3,4,5 를 만났을 경우 바뀌게 되는 방향
def obstacle(d, ob): # 장애물 만남 방향 조정
    if ob == 1:
        if d == 0:
            return 1
        elif d == 1:
            return 3
        elif d == 2:
            return 0
        elif d == 3:
            return 2

    elif ob == 2:
        if d == 0:
            return 3
        elif d == 1:
            return 0
        elif d == 2:
            return 1
        elif d == 3:
            return 2

    elif ob == 3:
        if d == 0:
            return 2
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        elif d == 3:
            return 1

    elif ob == 4:
        if d == 0:
            return 1
        elif d == 1:
            return 2
        elif d == 2:
            return 3
        elif d == 3:
            return 0
    
    elif ob == 5:
        if d == 0:
            return 1
        elif d == 1:
            return 0
        elif d == 2:
            return 3
        elif d == 3:
            return 2
    
# 음수, N 이상시 역방향
def wall(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d==3:
        return 2

def warp(x,y,d):
    num  =jido[x][y]-6
    if bh[num] == [x,y]:
        return [wh[num][0], wh[num][1], d]
    elif wh[num] == [x,y]:
        return [bh[num][0], bh[num][1], d]
# 웜홀 > 같은 좌표로 워프

def pinball(p,q,d):
    cnt = 0
    start = [p,q]
    dot = deque()
    dot.append([p,q,d])
    while True:
        x,y,d = dot.popleft()
        
        i = x + dx[d]
        j = y + dy[d]
        if i <-1 or N < i or j < -1 or N < j:
            continue

        if i <0 or i == N or j < 0 or j == N:
            dot.append([i,j,wall(d)])
            cnt += 1
        elif [i,j] == start or jido[i][j] == -1:
            return cnt
        
        elif jido[i][j] == 0:
            dot.append([i,j,d])

        elif jido[i][j] <= 5:
            dot.append([i,j,obstacle(d,jido[i][j])])
            cnt += 1
        else:
            dot.append(warp(i,j,d))
                
# -1 or 출발점 > 종료

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    jido = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    bh = [0]*5
    wh = [0]*5
    for i in range(N):
        for j in range(N):
            if jido[i][j] > 5:
                if bh[jido[i][j]-6]:
                    wh[jido[i][j]-6] = [i,j]
                else:
                    bh[jido[i][j]-6] = [i,j]

    for i in range(N):
        for j in range(N):
            if jido[i][j] == 0:
                for k in range(4):
                    a = pinball(i,j,k)
                    if a > ans:
                        ans = a
    
    print(f'#{tc} {ans}')