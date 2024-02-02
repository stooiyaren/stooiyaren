import sys
input = sys.stdin.readline

N = int(input())
A = [(x, y) for x in range(N//5+1) for y in range(N//3+1) if 5*x + 3*y == N]
mn = 5000

for i in A:
    if mn > sum(i):
        mn = sum(i)
if mn == 5000:
    mn = -1
print(mn)