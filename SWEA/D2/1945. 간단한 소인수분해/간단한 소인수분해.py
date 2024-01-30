def insu(n,a,b,c,d,e):
    if n%2 == 0:
        a += 1
        n //= 2
        return insu(n,a,b,c,d,e)
    elif n%3 == 0:
        b += 1
        n //=3
        return insu(n,a,b,c,d,e)
    elif n%5 == 0:
        c += 1
        n //=5
        return insu(n,a,b,c,d,e)
    elif n%7 == 0:
        d += 1
        n //=7
        return insu(n,a,b,c,d,e)
    elif n%11 ==0:
        e += 1
        n //=11
        return insu(n,a,b,c,d,e)
    else:
        return [a, b, c, d, e]

T = int(input())
for i in range(1, T+1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    bunhea = insu(N,a,b,c,d,e)
    print(f'#{i}',*bunhea)