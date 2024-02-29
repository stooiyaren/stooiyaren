def check(road):
    global X
    global N
    start = road[0]
    airstrip = [False] * N # 활주로 건설한 곳을 True를 기입해줍시다.
    for height in range(len(road)):
        if road[height] != start: # 한칸 이전 도로의 값과 현재 도로의 높이가 다르다면 평탄화를 해야합니다.
            if road[height] > start: # 도로가 높아졌다면
                if road[height] - start != 1: # 높이 차이가 1칸이 아니라면 기각입니다.
                    return 0
                else:
                    for p in range(1,X+1): # 활주로 건설을 위해 X의 거리가 필요합니다.
                        if height-p < 0: # 활주로를 이용해 높여야 하므로 x 거리만큼 확인합니다. 범위를 벗어나면 기각입니다.
                            return 0
                        if airstrip[height-p]: # 이미 활주로가 건설 되어 있다면 기각이예요
                            return 0
                        if road[height-p] != start: # 범위 안에 있다해도 이전과 높이가 다르다면 기각입니다.
                            return 0
                    for p in range(1,X+1): # 활주로 건설이 가능한 경우이니까 활주로를 지읍시다.
                        airstrip[height-p] = True
            else: # 도로가 낮아지는 경우입니다.
                if road[height] +1 != start: # 이전 도로보다 1칸 낮아진게 아니면 건설 불가 기각입니다.
                    return 0
                else:
                    for p in range(X): # 앞으로 높이가 같은지 확인해야합니다.
                        if height+p >= N: # 인덱스 N 이상은 범위를 벗어납니다.
                            return 0
                        if airstrip[height+p]: # 이미 활주로가 건설되어있다면 기각입니다.
                            return 0
                        if road[height+p] != start - 1:
                            return 0
                    for p in range(X): # 활주로 건설이 가능한 경우 활주로를 지읍시다. (높아지는 경우는 한칸 이전부터 낮아지는 경우는 지금부터 지어야 함을 명심합시다)
                        airstrip[height+p] = True
            start = road[height] # 활주로 확인이 끝난다면 현재의 값으로 높이를 변경해줍니다.
        else:
            pass # 한칸 이전과 현재 도로가 높이가 같다면 알바누 입니다.
    return 1 # 모든 과정을 통과한다면 1 추가... 합니다...

T = int(input())
for tc in range(1,T+1):
    N,X = map(int,input().split())
    feild = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in feild:
        ans += check(i)

    feild = list(map(list,zip(*feild)))

    for i in feild:
        ans += check(i)

    print(f'#{tc}', ans)