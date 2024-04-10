import heapq

def dijk(start):

        visited[start] = 0
        hq = [(0, start)]

        while hq:
                dist, start = heapq.heappop(hq)

                if dist > visited[start]:
                        continue

                for arrive, value in route[start]:
                        new_dist = dist + value
                        if visited[arrive] > new_dist:
                                visited[arrive] = new_dist
                                heapq.heappush(hq,(new_dist,arrive))
        
def dijk2(start):
        global X
        check = [float('inf')] * N

        check[start] = 0
        hq = [(0, start)]

        while hq:
                dist, start = heapq.heappop(hq)

                if dist > check[start]:
                        continue

                for arrive, value in route[start]:
                        new_dist = dist + value
                        if check[arrive] > new_dist:
                                check[arrive] = new_dist
                                heapq.heappush(hq,(new_dist,arrive))
        return check[X-1]

N,M,X = map(int,input().split())
route = [[] for _ in range(N)]
visited = [float('inf')] * N
ans = 0

for _ in range(M):
        s,e,t = map(int,input().split())
        route[s-1].append((e-1,t))

dijk(X-1)

for i in range(N):
        if i != (X-1):
                cnt = visited[i] + dijk2(i)
                if cnt > ans:
                        ans = cnt
print(ans)