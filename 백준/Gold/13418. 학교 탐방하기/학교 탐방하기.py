def kru():
        global check
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

        for value,start,end in route:

                if find_set(start) != find_set(end):
                        union(start,end)
                        if not value:
                                check += 1

N, M = map(int,input().split())

route = []
for _ in range(M+1):
        A,B,C = map(int,input().split())
        route.append((C,A,B))


route.sort(key = lambda x:x[0])

parent = list(range(N+1))
check = 0
kru()
cnt = check

check = 0
parent = list(range(N+1))
route.sort(reverse = True)
kru()

print(cnt**2-check**2)