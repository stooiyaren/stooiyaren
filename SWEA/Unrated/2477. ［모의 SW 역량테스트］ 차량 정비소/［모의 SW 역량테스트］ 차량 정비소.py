from collections import deque

T = int(input())
for tc in range(1,T+1):
    N,M,K,A,B = map(int,input().split())

    desk = list(map(int,input().split()))
    desking = [[] for _ in range(N)]

    fix = list(map(int,input().split()))
    fixing = [[] for _ in range(M)]

    arrive = deque(map(int,input().split()))
    person_number = 0
    second = 0 # 현재 시간

    waiting = deque()
    ans = [[] for _ in range(K)]

    while True:

        for i in ans:
            if len(i) != 2:
                break
        else:
            break

        for i in range(N): # 접수처를 반복
            if desking[i] and desking[i][0]: # 진행중이면 1초씩 따운
                desking[i][0] -= 1
                if not desking[i][0]:# 접수가 끝나면 정비청에 보내고  새로운 고객 투입
                    waiting.append(desking[i][1])                    
                    if arrive and arrive[0] <= second:
                        arrive.popleft()
                        ans[person_number].append(i)
                        desking[i] = [desk[i],person_number]
                        person_number += 1
            else: # 접수처가 비었다면
                if arrive and arrive[0] <= second:
                    arrive.popleft()
                    ans[person_number].append(i) # 나중에 +1 해줘야됨
                    desking[i] = [desk[i],person_number]
                    person_number += 1

        for i in range(M): # 정비청을 반복
            if fixing[i] and fixing[i][0]: # 정비중이면 1초씩 따운
                fixing[i][0] -= 1
                if not fixing[i][0]:
                    if waiting:
                        p = waiting.popleft()
                        ans[p].append(i)
                        fixing[i] = [fix[i],p]
            else:
                if waiting:
                    p = waiting.popleft()
                    ans[p].append(i)
                    fixing[i] = [fix[i],p]
                    
        second += 1

    cnt = 0
    for i in range(K):
        if ans[i] == [A-1,B-1]:
            cnt += i+1

    if cnt:
        print(f'#{tc} {cnt}')
    else:
        print(f'#{tc} -1')