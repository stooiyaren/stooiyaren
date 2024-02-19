N = int(input())
n = list(map(int,input().split()))
idx = list(range(1,N+1))
n = list(zip(n,idx))
stack = [n[-1]]
ans = [[0,0]] * (N+1)
for i in range(N-2,-1,-1):
    if n[i] < stack[-1]:
        stack.append(n[i])
    elif n[i] >= stack[-1]:
        while n[i] >= stack[-1]:
            expt = stack.pop()
            ans[expt[1]] = n[i]
            if not stack:
                break
        stack.append(n[i])
for i in range(1,len(ans)):
    print(ans[i][1], end = ' ')