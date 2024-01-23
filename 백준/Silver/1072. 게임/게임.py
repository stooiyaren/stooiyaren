import math
import sys
X, Y = map(int, sys.stdin.readline().split())
Z = Y*100//X
if Z == 99 or Z == 100:
    print(-1)
else:
    count = (abs((Z+1)*X-100*Y))/abs((99-Z))
    print(math.ceil(count))