N = int(input())
a = list(map(int, input().split()))
b = int(input())
count = 0
for k in range(len(a)):
     if a[k] == b:
          count += 1
print(count)