N = int(input())
S = list(map(int, input().split()))
d = [0]*N
n = 0
count = 0
m = max(S)
while n <= m:
    for i in range(N):
        if S[i] == n:
            d[i] = count
            count += 1
    n +=1
print(*d)