import sys
import math
input = sys.stdin.readline

N = int(input())
if N == 0:
    print(0)
else:
    n = int(math.log(N,5))
    cnt = 0
    for i in range(1,n+1):
        cnt += N//(5**i)
    print(cnt)