import heapq
import sys
input = sys.stdin.readline

def dijk():
    global K

    dist = [float('INF')] * (V+1)

    hq = [(0,K)]
    dist[K] = 0

    while hq:
        val, start = heapq.heappop(hq)

        for reach, value in graph[start]:
            if dist[reach] > val + value:
                dist[reach] = val + value
                heapq.heappush(hq,(val+value,reach))
    return dist

V,E = map(int,input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

route = dijk()

for i in range(1,V+1):
    if i == K:
        print(0)
    else:
        if route[i] == route[0]:
            print('INF')
        else:
            print(route[i])