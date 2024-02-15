import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    order= input()
    n = int(input())
    x = input().strip()
    if x == '[]':
        if 'D' in order:
            print('error')
        else:
            print('[]')
    else:
        x = [int(x) for x in x[1:-1].split(',')]
        x = deque(x)
        turn = 1
        ans = 1
        for i in order:
            if i == 'R':
                turn *= -1
            elif i == 'D':
                if not x:
                    ans = 0
                    break
                
                if turn > 0:
                    x.popleft()
                elif turn < 0:
                    x.pop()
        if not ans:
            print('error')
        else:
            if turn > 0 and x:
                n = x.pop()
                print('[',end='')
                for i in x:
                    print(f'{i},',end='')
                print(f'{n}', end='')
                print(']')
            elif turn < 0 and x:
                x = list(x)[::-1]
                n = x.pop()
                print('[',end='')
                for i in x:
                    print(f'{i},',end='')
                print(f'{n}', end='')
                print(']')
            else:
                print('[]')