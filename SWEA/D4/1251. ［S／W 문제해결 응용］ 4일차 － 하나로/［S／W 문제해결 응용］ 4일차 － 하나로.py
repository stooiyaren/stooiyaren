def kru(edges):
    def find_set(x):
        if parent[x] == x:
            return x
        return find_set(parent[x])

    def union(x, y):
        x = find_set(x)
        y = find_set(y)
        parent[x] = y

    mst = 0
    parent = list(range(N))

    for l, i, j in edges:
        if find_set(i) != find_set(j):
            union(i, j)
            mst += l

    return mst

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            l = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            edges.append((l * E, i, j))

    edges.sort()

    print(f'#{tc} {round(kru(edges))}')
