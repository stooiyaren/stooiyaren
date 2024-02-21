dx = [-1,1,0,0]                                                                     # 등산로를 찾는 상하좌우 델타좌표
dy = [0,0,-1,1]

def dfs(start):                                                                     # start = [i,j,cnt,height,chance]
    global K                                                                        # 돌깍는 능력과 answer list는 글로벌 변수로 받아옴
    global ans
                                                                                    # 기저조건 1. chance가 0인데 못내려가는경우 2. 돌을 깎아도 못가는 경우
    high = []
    for i in range(4):
        nx = start[0] + dx[i]
        ny = start[1] + dy[i]
        if 0 <= nx < N and 0 <= ny < N and [nx,ny] not in start[5]:                   # 상하좌우의 값이 방문한 적 없고 범위 내인경우
            high.append(jido[nx][ny])                                               # 각 방면 높이를 저장

    if not high:
        ans.append(start[2])
        return

    elif start[4] == 0 and start[3] <= min(high):                                     # 찬스가 없고 주변 높이가 내 높이보다 크거나 같다면 종료
        ans.append(start[2])                                                        # 못가니깐 answer list 에 append 하고 반환
        return
    
    elif start[4] == 1 and start[3] <= (min(high) - K):                             # 찬스가 있어도 주변 높이가 K를 깎아도 높으면 종료
        ans.append(start[2])                                                        # 만약 시간초과가 일어나면 ans과정은 global 변수비교로 구할 수 있음
        return
    
    else:                                                                           # 기저조건 끝 외에는 현재 height 저장하고 chance 저장하고 cnt 1씩 증가시키며 재귀
        for i in range(4):                                                          # 상하좌우 다시 탐색
            nx = start[0] + dx[i]
            ny = start[1] + dy[i]

            if [nx,ny] not in start[5] and 0 <= nx < N and 0 <= ny < N and jido[nx][ny] < start[3]: # 갈 수 있는 놈
                dfs([nx,ny, start[2]+1, jido[nx][ny], start[4],start[5] + [[nx,ny]]])

            elif start[4]:                                                          # chance가 있으면 확인하고 갈 수 있는놈에 추가 하는 메커니즘
                if [nx,ny] not in start[5] and 0 <= nx < N and 0 <= ny < N and jido[nx][ny] - K < start[3]:
                    dfs([nx, ny, start[2]+1, start[3]-1, 0,start[5] + [[nx,ny]]])

# ------------------------------------------------------------------------ function line -----------------------------------------
T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())                                     # N = 지도의 크기, K = 돌깍는 능력
    jido = [list(map(int,input().split())) for _ in range(N)]
    mx = 0                                                              # 최대값(산봉우리 높이)
    chance = 1                                                          # chance 는 한 번
    ans = []                                                            # 모든 경우 저장
    for i in range(N):
        for j in range(N):
            if jido[i][j] > mx:
                mx = jido[i][j]                                         # 지도 전체의 최댓값을 찾음

    jwapyo = []
    for i in range(N):
        for j in range(N):
            if jido[i][j] == mx:
                jwapyo.append([i,j,1,mx, chance,[[i,j]]])                       # 최대 높이를 좌표값에 리스트로 저장함 [산봉우리 x좌표, 산봉우리 y좌표, 등산로 횟수, 현재 높이, chance 기회]

    for i in jwapyo:                                     # 반환을 막기위해 False로 시작
        dfs(i)

    print(f'#{tc}', max(ans))