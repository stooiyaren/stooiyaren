dx = [-1,0,1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())
r,c,d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(N)]

cnt = 0 # 이때까지 청소한 칸 갯수
# 반시계 90도 = +1%4
now = [r,c]
trace = 2
while True:

    if not room[now[0]][now[1]]: # 1. 현재 칸이 청소되지 않은 경우 청소
        room[now[0]][now[1]] = trace
        trace += 1
        cnt += 1
    
    for i in range(3,-1,-1):
        nx = now[0]+dx[(d+i)%4]
        ny = now[1]+dy[(d+i)%4]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            d = (d+i)%4
            now = [nx,ny]
            break
    else: # 2. 4칸중 빈 칸이 없는 경우
        nx = now[0] + dx[(d+2)%4]
        ny = now[1] + dy[(d+2)%4]
        if 0<= nx < N and 0<= ny < M and room[nx][ny] != 1: # 1. 후진 할 수 있다면 후진하고 1번으로 돌아간다.
            now = [nx,ny]
            
        else: # 2. 뒤가 벽이라 후진할 수 없다면 작동을 멈춘다.
            break

print(cnt)