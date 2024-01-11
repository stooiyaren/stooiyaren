X = int(input())
N = int(input())
count = 0
for k in range(N):
     a, b = map(int, input().split())
     count += a * b

if count == X:
     print('Yes')
else:
     print('No')