import sys
input = sys.stdin.readline

N, R = map(int,input().split())
A = 1
B = 1
for i in range(N,N-R,-1):
    A *= i
for j in range(1,R+1):
    B *= j
print(A//B%10007)