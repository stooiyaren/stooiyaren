import sys
input = sys.stdin.readline

N = int(input())
n = list(map(int,input().split()))
if N == 1:
    print(-1)
elif N == 2:
    if n[1] >= n[0]:
        print(n[1], -1)
    else:
        print(-1,-1)
else:
    stack = [n[-1]]
    ans = [-1]
    for i in range(N-2,-1, -1):
        if n[i] < stack[-1]:
            ans.append(stack[-1])
            stack.append(n[i])
            
        elif n[i] >= stack[-1]:
            while n[i] >= stack[-1]:
                stack.pop()
                if not stack:
                    ans.append(-1)
                    break
            if stack:
                ans.append(stack[-1])
            stack.append(n[i])
    
    for i in range(len(ans)-1,-1,-1):
        print(ans[i], end = ' ')