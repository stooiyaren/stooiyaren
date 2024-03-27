import sys
input = sys.stdin.readline

def binary(i):
    global M, dist

    if sum(bit) > M: # 더 넘어감녀 바로 아웃
        return

    if i == len(chicken):
        if sum(bit) == M:
            ans = []
            for x,y in home:
                dis = []
                for p in range(len(chicken)):
                    if bit[p]:
                        dis.append(abs(chicken[p][0]-x) + abs(chicken[p][1]-y))
                ans.append(min(dis))
                if sum(ans) >= dist:
                    return

            dist = sum(ans)
            
            return
        else:
            return

    bit[i] = 1
    binary(i+1)
    bit[i] = 0
    binary(i+1)

N, M = map(int,input().split())
village = [list(map(int,input().split())) for _ in range(N)]

chicken = []
home = []

for i in range(N):
    for j in range(N):

        if village[i][j] == 2:
            chicken.append((i,j))
        if village[i][j] == 1:
            home.append((i,j))

# 치킨집은 치킨에 사람집은 홈에 저장됨
# 그럼 치킨집을 M개만큼 골라야됨
# 비트연산으로 고르겠습니데이

bit = [0] * len(chicken)
dist = N**3
binary(0)

print(dist)