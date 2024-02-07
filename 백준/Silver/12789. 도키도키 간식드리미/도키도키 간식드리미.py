import sys
input = sys.stdin.readline

N = int(input())
stack = list(map(int,input().split()))[::-1]
alley = []
cnt = 1
ans = 'Nice'
while cnt <= N:
    if stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1
        continue
    elif alley and alley[-1]== cnt:
        alley.pop()
        cnt += 1
        continue
    elif alley and cnt in alley:
        ans = 'Sad'
        break
    else:
        alley.append(stack.pop())
print(ans)