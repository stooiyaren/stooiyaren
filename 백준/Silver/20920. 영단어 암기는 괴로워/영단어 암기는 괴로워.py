import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pedia = {}
for i in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in pedia:
            pedia[word] += 1
        else:
            pedia[word] = 1

clean = [[] for _ in range(N+1)]
for key, value in pedia.items():
    clean[value].append(key)

for i in range(N,0,-1):
    if clean[i]:
        clean[i].sort(key=lambda x :(-len(x), x))
        for j in clean[i]:
            print(j)