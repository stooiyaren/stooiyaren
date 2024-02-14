import sys
import math
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
order = deque(map(int,input().split()))
num = deque(x for x in range(1,N+1))
cnt = 0
while order:
    n = order.popleft()
    if n == num[0]:
        num.popleft()
    elif num.index(n) >= math.ceil(len(num)/2):
        while n != num[0]:
            num.rotate(1)
            cnt += 1
        num.popleft()
    elif num.index(n) < math.ceil(len(num)/2):
        while n != num[0]:
            num.rotate(-1)
            cnt += 1
        num.popleft()
print(cnt)