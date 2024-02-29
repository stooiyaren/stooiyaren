def check(i,store):
    global w
    global h
    first = abs(i - store) # i(내가 있는 곳) 에서 store(가게가 있는 곳) 까지 가는 방법은 왼쪽, 오른쪽 두가지가 있습니다.
    if first > 2*(w+h) - first: # 최솟값을 구해야 하기 때문에 두 방법중 작은 값을 return 합니다.
        return 2*(w+h) - first
    else:
        return first

def where(you): # 0,0으로 부터 시계방향으로 얼마만큼 떨어져 있는지 계산하는 함수
    global w
    global h
    if you[0] == 1:
        return h+you[1]
    elif you[0] == 2:
        return 2*(w+h)-you[1]
    elif you[0] == 3:
        return h - you[1]
    elif you[0] == 4:
        return h+w+you[1]

w,h = map(int,input().split())
markets = int(input())
juso = []
for _ in range(markets):
    market = list(map(int,input().split()))
    juso.append(where(market))

mine = list(map(int,input().split()))
mine = where(mine)
cnt = 0
while juso:
    cnt += check(mine,juso.pop())
print(cnt)