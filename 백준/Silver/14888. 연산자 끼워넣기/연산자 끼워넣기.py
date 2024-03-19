def yearmountain(n,a,b,c,d,cnt): # 0, 0
    global N
    global mx
    global mn

    # 기저조건 n이 N이 될때까지만 반복합시다.
    if n == N:
        if cnt > mx:
            mx = cnt
        if cnt < mn:
            mn = cnt
        return
    if a:
        yearmountain(n+1,a-1,b,c,d,cnt+num[n])
    if b:
        yearmountain(n+1,a,b-1,c,d,cnt-num[n])
    if c:
        yearmountain(n+1,a,b,c-1,d,cnt*num[n])
    if d:
        yearmountain(n+1,a,b,c,d-1,int(cnt/num[n]))


N = int(input())
num = list(map(int,input().split()))
v,x,y,z = map(int,input().split())


mx = -1000000000
mn = 1000000000

yearmountain(1,v,x,y,z,num[0])
print(mx)
print(mn)