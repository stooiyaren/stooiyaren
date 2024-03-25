import sys
input = sys.stdin.readline

N = int(input())

friend = []

for i in range(N):
    weight, tall = map(int,input().split())
    friend.append((weight,tall))

ans = []
for i in range(N):
    cnt = 0
    for j in range(N):

        if i == j:
            continue

        if friend[i][0] < friend[j][0] and friend[i][1] < friend[j][1]:
            cnt += 1
    ans.append(cnt+1)

print(*ans)