def kru():

        def find_set(x):
                if x == parent[x]:
                        return x

                parent[x] = find_set(parent[x])
                return parent[x]

        def union(x,y):
                x = find_set(x)
                y = find_set(y)

                if x == y:
                        return

                elif x < y:
                        parent[x] = y
                elif x > y:
                        parent[y] = x

        for value, start, end in route:

                if find_set(start) != find_set(end):
                        union(start,end)
                        mst.append(value)

N, M = map(int,input().split()) # N : 집, M : 길

route = []

for _ in range(M):
        A,B,C = map(int,input().split())
        route.append((C,A-1,B-1))

parent = list(range(N))

route.sort()

mst = []

kru()

print(sum(mst)-max(mst))