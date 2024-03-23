from collections import deque

def bfs(begin):
    global K
    q = deque([begin])

    dist = [float('inf')] * 100001

    dist[begin] = 0

    while q:
        start = q.popleft()

        if start == K:
            return dist[start]

        if start +1 <100001 and dist[start]+1 < dist[start+1]:
            q.append(start+1)
            dist[start+1] = dist[start] +1
        if 0 <= start -1 and dist[start]+1 < dist[start-1]:
            q.append(start-1)
            dist[start-1] = dist[start] +1
        if start*2 <100001 and dist[start]+1 < dist[start*2]:
            q.append(start*2)
            dist[start*2] = dist[start] +1
                                   
N,K = map(int,input().split())
print(bfs(N))