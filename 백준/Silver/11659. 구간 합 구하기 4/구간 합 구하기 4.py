import sys
input = sys.stdin.readline

N, M = map(int,input().split())
n = list(map(int,input().split()))
stack = [0]*(N+1)
stack[0] = n[0]
for p in range(1,N):
    stack[p] = stack[p-1] + n[p]
        
for q in range(M):
    i, j = map(int,input().split())
    print(stack[j-1]-stack[i-2])