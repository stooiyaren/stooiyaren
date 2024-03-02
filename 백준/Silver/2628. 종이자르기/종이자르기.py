w, h = map(int,input().split())
m = int(input())
garo = [0,w]
sero = [0,h]
for _ in range(m):
    a, b = map(int,input().split())
    if a == 0:
        sero.append(b)
    elif a == 1:
        garo.append(b)
garo.sort()
sero.sort()
garom = []
serom = []
for i in range(len(garo)-1):
    garom.append(garo[i+1] - garo[i])
for i in range(len(sero)-1):
    serom.append(sero[i+1] - sero[i])

garom.sort()
serom.sort()
print(garom[-1] * serom[-1])