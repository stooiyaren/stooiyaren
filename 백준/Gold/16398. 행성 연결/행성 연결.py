def kru():
        global ans
        
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

        for value, start, end in flow:
                
                if find_set(start) != find_set(end):
                        union(start,end)
                        ans += value


        

N = int(input())

planet = [list(map(int,input().split())) for _ in range(N)]

ans = 0

flow = []
for i in range(N):
        for j in range(N):
                if i != j:
                        flow.append((planet[i][j],i,j))

flow.sort()

parent = list(range(N))
kru()
print(ans)