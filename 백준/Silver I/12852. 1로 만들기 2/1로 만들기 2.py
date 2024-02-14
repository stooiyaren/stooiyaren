import sys
input = sys.stdin.readline

N = int(input())
d = [0] * (N+1)
stack = [0] * (N+1)

if N == 1:
    print(0)
    print(1)
elif N == 2:
    print(1)
    print(2,1)
elif N == 3:
    print(1)
    print(3,1)
else:
    d[1] = 0
    d[2] = 1
    d[3] = 1
    
    stack[1] = [1]
    stack[2] = [2,1]
    stack[3] = [3,1]
    for i in range(4,N+1):
        
        a = d[i-1]+1
        d[i] = a
        stack[i] = [i] + stack[i-1]
        if i % 2 == 0:
            b = d[i//2]+1
            if d[i] > b:
                d[i] = b
                stack[i] = [i] + stack[i//2]
        if i%3 == 0:
            c = d[i//3]+1
            if d[i] > c:
                d[i] = c
                stack[i] = [i] + stack[i//3]
    
    print(d[N])
    print(*stack[N])  