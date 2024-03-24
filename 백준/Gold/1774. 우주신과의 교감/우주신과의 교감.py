import heapq
import sys
input = sys.stdin.readline

def prim(start):
    hq = [(0,start)]
    mst = [0]*N

    sum_weight = 0

    while hq:
        weight, now = heapq.heappop(hq)

        if mst[now]:
            continue

        mst[now] = 1

        sum_weight += weight

        for wei, end in graph[now]:
            if mst[end]:
                continue
            heapq.heappush(hq,(wei, end))
    return sum_weight


N, M = map(int,input().split())

graph = [[] for _ in range(N)]

starx = [0]*(N)
stary = [0]*(N)
for i in range(N):
    starx[i],stary[i] = map(int,input().split())

for i in range(N-1):
    for j in range(i+1, N):
        L = ((starx[i]-starx[j])**2 + (stary[i] - stary[j])**2)**0.5
        graph[i].append((L,j))
        graph[j].append((L,i))


for i in range(M):
    start, end = map(int,input().split())
    graph[start-1].append((0,end-1))
    graph[end-1].append((0,start-1))


print(format(prim(0),".2f"))