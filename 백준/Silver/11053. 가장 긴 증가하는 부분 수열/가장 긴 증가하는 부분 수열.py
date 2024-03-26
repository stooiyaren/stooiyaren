import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
dp = [0]*N

for i in range(N):
    cnt = 0
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[j] > cnt:
                cnt = dp[j]

    dp[i] = cnt + 1

print(max(dp))