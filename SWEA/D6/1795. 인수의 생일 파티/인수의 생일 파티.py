import heapq

def dijsktra(graph, start):
    # 최단 거리 저장 리스트
    dist = [float('inf')] * (N+1)

    dist[start] = 0
    mheap = [(0,start)]

    while mheap:
        cost, node = heapq.heappop(mheap)

        if cost > dist[node]:
            continue

        for nxt, w in graph[node]:
            new_dist = dist[node] + w
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(mheap, (new_dist, nxt))

    return dist

def dijsktraa(graph, start,end):
    # 최단 거리 저장 리스트
    dist = [float('inf')] * (N+1)

    dist[start] = 0
    mheap = [(0,start)]

    while mheap:
        cost, node = heapq.heappop(mheap)

        if cost > dist[node]:
            continue

        for nxt, w in graph[node]:
            new_dist = dist[node] + w
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(mheap, (new_dist, nxt))

    return dist[end]



T = int(input())
for tc in range(1,T+1):
    N, M, X = map(int,input().split())
    
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        x,y,c = map(int,input().split())
        graph[x].append((y,c))

    route = dijsktra(graph,X)

    ans = 0
    for i in range(1,N+1):
        if i == X:
            continue
        if ans < route[i] + dijsktraa(graph,i,X):
            ans = route[i] + dijsktraa(graph,i,X)
    
    print(f'#{tc} {ans}')