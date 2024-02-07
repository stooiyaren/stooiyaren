from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int ,input().split()))
queue = deque([B[idx] for idx in range(N) if A[idx] == 0])
M = int(input())
C = list(map(int,input().split()))

if not queue:
    print(*C)
else:
    for i in C:
        item = queue.pop()
        queue.appendleft(i)
        print(item, end = ' ')