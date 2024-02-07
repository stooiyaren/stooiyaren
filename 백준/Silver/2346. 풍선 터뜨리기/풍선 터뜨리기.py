from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
balloon = deque(map(int,input().split()))
seq = deque( i for i in range(1,N+1))
ans = []
while balloon:
    n = balloon.popleft()
    ans.append(seq.popleft())
    
    if n > 0:
        balloon.rotate(-n+1)
        seq.rotate(-n+1)
    elif n < 0:
        balloon.rotate(-n)
        seq.rotate(-n)
print(*ans)