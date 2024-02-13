import sys
input = sys.stdin.readline

N = int(input())
n = set(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

count = []
for i in m:
   if i in n:
      count.append(1)
   else:
      count.append(0)
print(*count)