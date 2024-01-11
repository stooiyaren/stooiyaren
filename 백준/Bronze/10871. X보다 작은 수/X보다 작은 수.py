N, X = map(int, input().split())
a = list(map(int, input().split()))
b = []
count = 0
for k in range(len(a)):
     if a[k] < X:
          b.append(a[k])
print(*b)