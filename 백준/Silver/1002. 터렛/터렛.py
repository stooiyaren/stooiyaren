import math
import sys
T = int(sys.stdin.readline())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if d == 0 and r1==r2:
        print(-1)
    elif abs(r1-r2) == d or r1 + r2 == d:
        print(1)
    elif abs(r1-r2) < d < r1 + r2:
        print(2)
    else:
        print(0)
