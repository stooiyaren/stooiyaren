a = 1
b = 0
while a != b:
     c, d = map(int, input().split())
     if c == b and b == 0:
          break
     print(c+d)