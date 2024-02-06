import sys
from collections import deque
input = sys.stdin.readline
stack = deque()
num = 1
ans = deque()
cnt = 0
N = int(input())

for i in range(N):
    n = int(input())
    if n >= num or n in stack:
        if n >= num:
            while n >= num:
                stack.append(num)
                ans.append('+')
                num += 1
            stack.pop()
            ans.append('-')
        if n in stack:
            if n == stack[-1]:
                stack.pop()
                ans.append('-')
            else:
                cnt = -1
                break
    else:
        cnt = -1
        break
if cnt == -1:
    print('NO')
else:
    for i in ans:
        print(i)