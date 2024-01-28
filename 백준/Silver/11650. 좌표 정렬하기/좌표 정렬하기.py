import sys
input = sys.stdin.readline

N = int(input())
x = ['']*N
y = ['']*N
for i in range(N):
    x[i],y[i]=map(int, input().split())

dot =sorted(list(zip(x,y)))
for i in dot:
    print(i[0],i[1])