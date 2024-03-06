import sys
input = sys.stdin.readline

for _ in range(4):
    x1,y1,x2,y2,i1,j1,i2,j2 = list(map(int,input().split()))
    ans = 'a'

    a = (x2 == i1)
    b = (y2 == j1)
    c = (i2 == x1)
    d = (j2 == y1)

    if x2 < i1 or y2 < j1 or i2 < x1 or j2 < y1:
        ans = 'd'

    elif a or c:
        if b or d:
            ans = 'c'
        else:
            ans = 'b'
    elif b or d:
        ans = 'b'
    else:
        ans = 'a'
    print(ans)