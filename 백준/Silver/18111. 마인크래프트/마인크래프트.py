import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())

land = [list(map(int,input().split())) for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(M):
        cnt += land[i][j]
best_floor = (cnt+B)//(N*M)

floor = 0
second = float('inf')
for i in range(best_floor,-1,-1):
    seco = 0
    for p in range(N):
        for q in range(M):

            if land[p][q] > i :
                seco += 2 * (land[p][q] - i)
            else:
                seco += i - land[p][q]

    if second > seco:
        second = seco
        floor = i

print(second, floor)