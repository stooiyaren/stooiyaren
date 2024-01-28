import sys
input = sys.stdin.readline

N = int(input())
x = ['']*N
y = ['']*N
for i in range(N):
    x[i],y[i]=map(int, input().split())

dot =sorted(list(zip(y,x)))
for i in dot:
    print(i[1],i[0])