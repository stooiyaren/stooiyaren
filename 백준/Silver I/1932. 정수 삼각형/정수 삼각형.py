import sys
input = sys.stdin.readline

N = int(input())
d = [0]*(N+1)
if N == 1:
    print(int(input()))
else:
    d[1] =int(input())
    for i in range(2,N+1):
        a = list(map(int,input().split()))
        a = [0] + a        
        for j in range(1,i+1):
            a[j] = max((d[j-1]+a[j]),(d[j]+a[j]))
        d = a + [0] * N
    print(max(d))