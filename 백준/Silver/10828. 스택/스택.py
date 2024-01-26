import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range (N):
    order = list(input().split())
    if order[0] == 'push':
        stack.append(int(order[1]))
    elif order[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])