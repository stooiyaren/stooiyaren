import sys
input = sys.stdin.readline

N = int(input())
sil = str(input().rstrip())

ans = 0

for i in range(N):
    ans += (ord(sil[i])-96) * 31**i
print(ans%1234567891)