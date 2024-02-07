from collections import deque
import sys
input = sys.stdin.readline

que = deque()
N = int(input())
for _ in range(N):
    order = list(input().split())

    if order[0] == 'push':
        que.appendleft(order[1])
    
    elif order[0] == 'pop':
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
            print(que[-1])
    
    elif order[0] == 'back':
        if not que:
            print(-1)
        else:
            print(que[0])