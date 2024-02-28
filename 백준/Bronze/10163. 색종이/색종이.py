flat = [[0]*1001 for _ in range(1001)]
n = int(input())
for i in range(1,n+1):
    x,y,w,h = map(int,input().split())

    for p in range(w):
        for q in range(h):
            flat[x+p][y+q] = i

for i in range(1,n+1):
    cnt = 0
    for p in range(1001):
        for q in range(1001):
            if flat[p][q] == i:
                cnt += 1
    print(cnt)