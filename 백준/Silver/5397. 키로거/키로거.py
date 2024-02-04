from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    fake = list(input().strip())
    password = deque()
    cursor = 0
    for i in fake:
        if i == '<':
            if cursor != 0:
                password.rotate(1)
                cursor -= 1
        elif i == '>':
            if cursor != len(password):
                password.rotate(-1)
                cursor += 1
        elif i == '-':
            if cursor != 0 and password:
                password.pop()
                cursor -= 1
        else:
            cursor += 1
            password.append(i)
    password.rotate(cursor)
    print(''.join(password))