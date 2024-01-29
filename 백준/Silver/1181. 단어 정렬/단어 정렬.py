import sys
input = sys.stdin.readline

N = int(input())
result = {}
for i in range(N):
    n = input()
    if len(n) not in result:
        result[len(n)] = [n]
    else:
        result[len(n)].append(n)

line = sorted(list(result.keys()))
for i in line:
    result[i] = list(set(result[i]))
    result[i].sort()
    for j in result[i]:
        print(j[:-1])