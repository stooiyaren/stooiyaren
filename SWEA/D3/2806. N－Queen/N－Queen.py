def game(x,y_list): # 게임의 변수로 (x 값, 이제껏 사용한 y의 값) 를 받아옵니다.
    global N
    if x == N: # x가 N이 되면 (N-1까지 존재하는 배열 모두를 탐색 했다면)
        global cnt
        cnt += 1 # 현재 점수를 최고 점수와 비교해서 갱신하고 종료합니다.
        return

    for i in range(N): # N번 반복하며 y의 값을 정해줍니다.
        if check(x,i,y_list): # 만약 y좌표를 사용한 적 없고, 목표가 음수가 아니라면
            y_list.append([x,i]) # y리스트에 i를 더하고
            game(x+1,y_list) # 다음 줄로 넘어갑니다. (x+1)
            y_list.pop() # 재귀가 끝나고 돌아오면 y리스트 제거와 점수 제거를 해줍니다.

def check(x,j,y):
    for i in range(len(y)):
        if j == y[i][1] or abs(x-y[i][0]) == abs(j-y[i][1]):
            return False
    else:
        return True

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    for i in range(N): # 0번째 줄을 N까지 반복하며 시작점을 정합니다.
        y = [[0,i]]
        game(1, y)
    
    print(f'#{tc}',cnt)