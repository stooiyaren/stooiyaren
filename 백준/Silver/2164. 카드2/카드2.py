from collections import deque
import sys
input = sys.stdin.readline

N =deque(range(1,int(input())+1))

while len(N) >1:
    N.popleft()
    N.append(N.popleft())

print(*N)