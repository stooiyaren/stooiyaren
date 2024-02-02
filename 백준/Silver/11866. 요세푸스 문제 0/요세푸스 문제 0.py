from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
table = deque(range(1,N+1))
killed = []

while table:
    table.rotate(-(K-1))
    killed.append(table.popleft())
print('<' +', '.join(map(str,killed)) +'>' )