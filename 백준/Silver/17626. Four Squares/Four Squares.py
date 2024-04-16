from math import sqrt

N = int(input())
n = int(sqrt(N))
dp = [4] * (N+1)
square = []

for i in range(1,n+1):
        dp[i**2] = 1
        square.append(i*i)

sq = len(square)
two = []
for i in range(sq):
        for j in range(sq):
                tw = square[i]+square[j]
                if tw <= N and dp[tw] != 1:
                        two.append(tw)
                        dp[tw] = 2

wt = len(two)
for i in range(sq):
        for j in range(wt):
                th = square[i] + two[j]
                if th <=N and dp[th] ==4:
                        dp[th] = 3
print(dp[N])