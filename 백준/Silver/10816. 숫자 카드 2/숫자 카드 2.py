import sys
input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

dic = {}
for i in n:
    if i not in dic:
        dic.setdefault(i)
        dic[i] = 1
    else:
        dic[i] += 1

for j in range(M):
    m[j] = dic.get(m[j],0)
print(*m)