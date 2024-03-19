
T = int(input())
for tc in range(1,T+1):
    d,m,tm,y = map(int,input().split())
    schedule = list(map(int,input().split()))

    schedule = [0] + schedule # 0번째 달을 추가

    for i in range(13): # 0달 + 12달 비교
        if schedule[i]*d > m: # 일일 비용과 월 비용중 싼 가격으로 갱신
            schedule[i] = m
        else:
            schedule[i] *= d
    
    # 세 달 비교
    schedule[2] = schedule[1] + schedule[2]
    for i in range(3,13):
        schedule[i] = min(schedule[i]+schedule[i-1], tm + schedule[i-3])
    
    if schedule[12] > y:
        ans = y
    else:
        ans = schedule[12]
    print(f'#{tc} {ans}')