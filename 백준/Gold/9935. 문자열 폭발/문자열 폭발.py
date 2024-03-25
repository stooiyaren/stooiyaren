import sys
input = sys.stdin.readline

letter = str(input().rstrip())
bomb = str(input().rstrip())
b = len(bomb)
stack = []
for i in letter:
    stack.append(i)

    if len(stack) >= b:
        for j in range(b):
            if stack[-b+j] != bomb[j]:
                break
        else:
            for j in range(b):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')