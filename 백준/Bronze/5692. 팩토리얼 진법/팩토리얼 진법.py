def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)

import sys
input = sys.stdin.readline
while True:
    N = str(input())
    length = len(N)
    N = int(N)
    count = 0
    if N == 0:
        break

    for i in range(1,length+1):
        count += N%10 * facto(i)
        N = N//10
    print(count)