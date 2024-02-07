import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    important = deque(map(int,input().split()))
    cnt = 0
    num = 0
    while True:
        if important[0] == max(important):
            if M == 0:
                cnt += 1
                break
            important.popleft()
            M -= 1
            cnt += 1
        else:
            important.rotate(-1)
            if M == 0:
                M = len(important) - 1
            else:
                M -= 1
    print(cnt)