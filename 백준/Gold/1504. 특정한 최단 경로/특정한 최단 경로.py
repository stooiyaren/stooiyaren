import heapq

def dijk(start,end, end2):

    dist = [float('INF')] * (N+1)

    hq = [(0,start)]
    dist[start] = 0

    while hq:
        val, start = heapq.heappop(hq)

        for reach, value in graph[start]:
            if dist[reach] > val + value:
                dist[reach] = val + value
                heapq.heappush(hq,(val+value,reach))
    return dist[end], dist[end2]

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())

x1, x2 = dijk(1,v1,v2)
y1, emty = dijk(v1,v2,N)
z1, z2 = dijk(N,v1,v2)

ans = min(x1+y1+z2,x2+y1+z1)
check = float('INF')
if ans == check:
    print(-1)
else:
    print(ans)