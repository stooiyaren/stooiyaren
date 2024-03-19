def yearmountain(n,a,b,c,d,cnt): # 연산 (숫자, 더하기, 뻬기, 곱하기, 나누기, 연산합)
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
    # n이 N이 되기 전까지 각 연산을 해주고 n+1 하고 cnt에 연산해줍니다.
    if a: # 더하기가 있다면
        yearmountain(n+1,a-1,b,c,d,cnt+num[n]) # n +1 , a하나 써서 cnt에 num[n] 더해주기
    if b:
        yearmountain(n+1,a,b-1,c,d,cnt-num[n])
    if c:
        yearmountain(n+1,a,b,c-1,d,cnt*num[n])
    if d:
        yearmountain(n+1,a,b,c,d-1,int(cnt/num[n]))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    v,x,y,z = map(int,input().split())
    num = list(map(int,input().split()))

    mx = -100000000
    mn = 100000000

    yearmountain(1,v,x,y,z,num[0])
    print(f'#{tc} {mx-mn}')