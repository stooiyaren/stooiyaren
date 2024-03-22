# 배

# N대의 크레인
# 1분에 박스 1개
# 시간의 최솟값
import sys
input = sys.stdin.readline

N = int(input())
crain = list(map(int,input().split()))
M = int(input())
box = list(map(int,input().split()))

crain.sort(reverse = True)
box.sort(reverse = True)

if crain[0] < box[0]:
    print(-1)
else:
    cnt = 0
    while box:

        for i in crain:
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
        cnt += 1
    print(cnt)