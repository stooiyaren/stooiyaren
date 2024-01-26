N = int(input())
x=[0]*N
y=[0]*N
for i in range(N):
    x[i], y[i] = map(int, input().split())

print((max(x)-min(x))*(max(y)-min(y)))