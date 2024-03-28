import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1] # 상하좌우 델타 좌표

def bfs(x,y):
    q = deque()
    q.append((x,y))
    village[x][y] = 0 # 확인한 곳은 0으로 바꾸겠습니다 (방문처리)
    home = 1 # 단지에서 발견한 집

    while q: # q가 있는동안 반복
        x,y = q.popleft()

        for i in range(4): # 상하좌우 확인
            di = x+dx[i]
            dj = y+dy[i]
            if 0 <= di < N and 0 <= dj < N and village[di][dj] == 1:
                q.append((di,dj))
                village[di][dj] = 0
                home += 1
    ans.append(home)
    return

# --------------------------함수 --------------------


N = int(input())
village = [list(map(int,input().rstrip())) for _ in range(N)]
cnt = 0 # 단지의 수를 저장하는 변수
ans = [] # 각 단지 내 집의 수를 저장하는 변수

for i in range(N): # 마을 전체를 순환하며 단지를 찾습니다.
    for j in range(N):
        if village[i][j] == 1: # 찾았다면 bfs를 실행
            bfs(i,j)
            cnt += 1

print(cnt)
ans.sort()
for i in ans:
    print(i)