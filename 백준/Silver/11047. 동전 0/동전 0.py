import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coin = []
for i in range(N):
    coin.append(int(input()))


cnt = 0

for i in range(N-1,-1,-1):
    if coin[i] <= K:
        cnt += K//coin[i]
        K = K%coin[i]

    if K == 0:
        break

print(cnt)