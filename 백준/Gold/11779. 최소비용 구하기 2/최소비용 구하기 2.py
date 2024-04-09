import heapq

def dijk(start):
    hq = []

    heapq.heappush(hq,(0,start))
    price[start] = 0
    trace[start].append(start+1)
    
    while hq:
        value, now = heapq.heappop(hq)

        if value > price[now]:
            continue

        for arrive, pri in route[now]:
            new_price = price[now]+pri
            if new_price < price[arrive]:
                price[arrive] = new_price
                heapq.heappush(hq,(new_price,arrive))
                trace[arrive] = trace[now] + [arrive+1]


N = int(input())
M = int(input())

route = [[] for _ in range(N)]
price = [float('inf')]*N
trace = [[] for _ in range(N)]
for _ in range(M):
    s,e,p = map(int,input().split())
    route[s-1].append((e-1,p))

start, end = map(int,input().split())
dijk(start-1)

print(price[end-1])
print(len(trace[end-1]))
print(*trace[end-1])