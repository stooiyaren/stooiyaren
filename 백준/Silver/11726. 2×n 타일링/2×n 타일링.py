n = int(input())
d = [0]*1001
d[1],d[2] = 1, 2
if n == 1:
    print(d[1])
elif n == 2:
    print(d[2])
else:
    for i in range(3,n+1):
        d[i] = (d[i-1] + d[i-2])%10007
    print(d[n])