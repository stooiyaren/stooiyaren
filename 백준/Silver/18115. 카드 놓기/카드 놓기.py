from collections import deque
import sys
N = int(sys.stdin.readline())
sit = list(map(int, sys.stdin.readline().split()))
sit.reverse()
cnt = 1
deck = deque()
for i in sit:
    if i == 1:
        deck.appendleft(cnt)
    elif i ==2:
        deck.insert(1,cnt)
    elif i ==3:
        deck.append(cnt)
    cnt += 1
print(*deck)