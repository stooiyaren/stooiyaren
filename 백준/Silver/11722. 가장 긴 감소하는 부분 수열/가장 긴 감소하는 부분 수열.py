import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
ar = arr[::-1]
#dp = [0]*N
dpr = [0]*N

for i in range(N):
#    cnt = 0
    cnt2 = 0
    for j in range(i):
#        if arr[i] > arr[j]:
#            if dp[j] > cnt:
#                cnt = dp[j]
        if ar[i] > ar[j]:
            if dpr[j] > cnt2:
                cnt2 = dpr[j]
    
#    dp[i] = cnt + 1
    dpr[i] = cnt2 + 1
#ans = [0] *N
#for i in range(N):
#    ans[i] =dp[i]+dpr[N-i-1]
print(max(dpr))
   