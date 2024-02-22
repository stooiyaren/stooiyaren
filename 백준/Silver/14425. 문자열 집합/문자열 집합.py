munja = []
cnt = 0
N, M = map(int,input().split())
for i in range(N):
    munja.append(input())

for i in range(M):
    check = input()
    if check in munja:
        cnt += 1

print(cnt)