#from collections import deque
N = int(input())
P = list(map(int,input().split()))
P.sort(reverse = True)
cnt = 0
for i in range(len(P)):
    cnt += P[-1] * len(P)
    P.pop()
print(cnt)