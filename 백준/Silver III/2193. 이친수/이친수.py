N = int(input())
d = [0]*(N+1)
if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    d[1] = 1
    d[2] = 1
    for i in range(3,N+1):
        d[i] = d[i-1] + d[i-2]
    print(d[N])