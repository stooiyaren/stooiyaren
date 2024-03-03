N = int(input())
roof = [0] * 1001
for i in range(N):
    x,y = map(int,input().split())
    roof[x] = y

fmx = 0
bmx = 0
cnt = roof.count(max(roof))
lcnt = 0
rcnt = 1000
ans = 0
if cnt == 1:
    while fmx != max(roof):
        if roof[lcnt] > fmx:
            fmx = roof[lcnt]
        ans += fmx        

        lcnt += 1
        
    while bmx != max(roof):
        if roof[rcnt] > bmx:
            bmx = roof[rcnt]
        ans += bmx

        rcnt -= 1
    print(ans - max(roof))
else:
    while fmx != max(roof):
        if roof[lcnt] > fmx:
            fmx = roof[lcnt]
        ans += fmx        

        lcnt += 1
        
    while bmx != max(roof):
        if roof[rcnt] > bmx:
            bmx = roof[rcnt]
        ans += bmx

        rcnt -= 1

    ans += max(roof) * (rcnt-lcnt+1)

    print(ans)