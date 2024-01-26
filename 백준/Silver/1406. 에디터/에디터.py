import sys
from collections import deque
input = sys.stdin.readline

que = deque(input().strip())
cursor = 0
N = int(input())
for i in range (N):
    order = input().split()
    if order[0] == 'L':
        if cursor == len(que):
            continue
        else:
            que.appendleft(que.pop())
            cursor += 1
    elif order[0] == 'D':
        if cursor == 0:
            continue
        else:
            que.append(que.popleft())
            cursor -= 1        
    elif order[0] == 'B':
        if cursor == len(que):
            continue
        else:
            que.pop()
    elif order[0] == 'P':
        que.append(order[1])
que = list(que)
que = que[cursor:] + que[:cursor]
print("".join(que))