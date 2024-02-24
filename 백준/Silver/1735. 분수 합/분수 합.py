import math

A, B = map(int,input().split())
C, D = map(int,input().split())
a = A*D + B*C
b = B*D
c = math.gcd(a,b)
print((a//c), (b//c))