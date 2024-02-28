whole = [[0]*100 for _ in range (100)]

for i in range(4):
    a,b,c,d = map(int,input().split())

    for p in range(a,c):
        for q in range(b,d):
            whole[p][q] = 1
ans = 0
for i in whole:
    ans += sum(i)

print(ans)