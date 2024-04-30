n, k = map(int,input().split())
coin = []
for _ in range(n):
    value = int(input())
    if value <= k:
        coin.append(value)
coin.sort()

dp = [0] * (k+1)

for i in coin:
    dp[i] += 1

    for j in range(i,k+1):
        dp[j] += dp[j-i]
    
print(dp[k])  