from collections import deque

def right(turn, turning):
    if turn == 4: # 맨 오른쪽이면 조사 종료
        gearset[turn].rotate(turning)
        return

    if gearset[turn][2] != gearset[turn+1][6]: 
        gearset[turn].rotate(turning) # 돌리고
        right(turn+1,turning*-1) # 재귀
    else:
        gearset[turn].rotate(turning)


def left(turn,turning):
    if turn == 1: # 맨 왼쪽이면 조사 종료
        gearset[turn].rotate(turning)
        return

    if gearset[turn][6] != gearset[turn-1][2]: # 6번째 바퀴랑 2번째 바퀴가 다르면
        gearset[turn].rotate(turning) # 돌리고
        left(turn-1,turning*-1) # 재귀
    else:
        gearset[turn].rotate(turning)
    
    

T = int(input())
for tc in range(1,T+1):
    K = int(input())
    gear1 = deque(map(int,input().split()))
    gear2 = deque(map(int,input().split()))
    gear3 = deque(map(int,input().split()))
    gear4 = deque(map(int,input().split()))
    
    gearset = { 1 : gear1, 2 : gear2, 3: gear3, 4:gear4}


    for i in range(K): # 게임을 시작하죠
        turn, turning = map(int,input().split())
        right(turn,turning)
        gearset[turn].rotate(turning*-1)
        left(turn,turning)

    # 게임이 끝났을때
    score = 0    
    if gear1.popleft():
        score += 1
    if gear2.popleft():
        score += 2
    if gear3.popleft():
        score += 4
    if gear4.popleft():
        score += 8
    print(f'#{tc} {score}')