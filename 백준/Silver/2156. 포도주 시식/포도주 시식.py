n = int(input())
wine = [0]*n
for i in range(n):
    wine[i] = int(input())
if n==1:
    print(wine[0])
elif n==2:
    print(wine[0] + wine[1])
elif n==3:
    print(max(wine[0] + wine[2], wine[1] + wine[2], wine[0]+ wine[1]))
else:
    dp = [0]*n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2],wine[0]+wine[1])
    # dp[3] = max(wine[0]+wine[2]+wine[3], wine[0]+wine[1]+wine[3])
    # dp[4] = max(wine[0]+wine[2]+wine[4], wine[0]+wine[1]+wine[3]+wine[4])
    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2]+wine[i], dp[i-3] + wine[i-1] + wine[i])

    print(max(dp))