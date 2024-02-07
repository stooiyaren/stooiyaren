from collections import deque
import sys
input = sys.stdin.readline

deck = deque()
N = int(input())
for _ in range(N):
    order = list(input().split())

    if order[0] == '1':
        deck.appendleft(order[1])

    elif order[0] == '2':
        deck.append(order[1])
    
    elif order[0] == '3':
        if not deck:
            print(-1)
        else:
            print(deck.popleft())

    elif order[0] == '4':
        if not deck:
            print(-1)
        else:
            print(deck.pop())

    elif order[0] == '5':
        print(len(deck))
    
    elif order[0] == '6':
        if not deck:
            print(1)
        else:
            print(0)
    
    elif order[0] == '7':
        if not deck:
            print(-1)
        else:
            print(deck[0])
    
    elif order[0] == '8':
        if not deck:
            print(-1)
        else:
            print(deck[-1])