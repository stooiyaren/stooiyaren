import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
que = deque()
for i in range (N):
    order = list(input().split())
    if order[0] == 'push_front':
        que.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        que.append(int(order[1]))        
    elif order[0] == 'pop_front':
        if not que:
            print(-1)
        else:
            print(que.popleft())
    elif order[0] == 'pop_back':
        if not que:
            print(-1)
        else:
            print(que.pop())            
    elif order[0] == 'size':
        print(len(que))
    elif order[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif order[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[-1])