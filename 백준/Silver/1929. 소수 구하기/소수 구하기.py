import sys
input = sys.stdin.readline

M, N = map(int,input().split())
number = list(range(N+1))
prime = []
for i in range(2,N+1):
    if number[i] == 0:
        continue
    for j in range(i*i,N+1,i):
        number[j] = 0

for i in number:
    if i != 0 and i != 1 and M<=i :
        print(i)