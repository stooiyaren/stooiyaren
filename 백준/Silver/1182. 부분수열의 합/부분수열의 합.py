def f(i, k, total):
    global S
    global cnt
    if i == k:
        if total == S:
            cnt += 1 
                
    else:
        bit[i] = 1
        f(i+1, k, total + n[i])
        bit[i] = 0
        f(i+1, k, total)
        
import sys
input = sys.stdin.readline

N, S = map(int,input().split())
n = list(map(int,input().split()))
cnt = 0
bit= [0] * N
f(0,N,0)
if S == 0:
    print(cnt-1)
else:
    print(cnt)