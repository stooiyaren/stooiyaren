n, m = map(int,input().split())
dudo = []
for _ in range(n):
    dudo.append(input())
bodo = []
for _ in range(m):
    bodo.append(input())
dudo = set(dudo)
bodo = set(bodo)

dudobodo = list(set.intersection(dudo,bodo))
dudobodo.sort()
print(len(dudobodo))
for i in dudobodo:
    print(i)
