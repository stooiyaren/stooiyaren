import sys
input = sys.stdin.readline


x = int(input())
coin = [0]*(x+1)
for i in range(2,x+1):
    coin[i] = coin[i-1] + 1
    if i % 3 == 0 and coin[i//3] < coin[i]:
            coin[i] = coin[i//3]+1
    if i % 2 == 0 and coin[i//2] < coin[i]:
            coin[i] = coin[i//2]+1
print(coin[x])