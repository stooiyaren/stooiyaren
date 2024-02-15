from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

yose = deque(range(1,N+1))
puse = []
while yose:
	yose.rotate(-(K-1))
	puse.append(yose.popleft())
puse = map(str,puse)
result = ', '.join(puse)
print(f'<{result}>')