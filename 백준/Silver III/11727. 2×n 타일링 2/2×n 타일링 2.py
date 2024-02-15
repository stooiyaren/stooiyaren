n = int(input())

d = [0] * 1001

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    d[1] = 1
    d[2] = 3
    for i in range(3,n+1):
        d[i] = (d[i-1] + 2*d[i-2])%10007
    
    print(d[n])