import sys
input = sys.stdin.readline

stack = []

K = int(input())
for i in range(K):
    N = int(input())
    if N == 0: # 지울 수 있는 수가 있는 경우에만 0이 나온다고 문제에서 지정.
        stack.pop()
    else:
        stack.append(N)
print(sum(stack))