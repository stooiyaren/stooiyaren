a, b, c = map(int, input().split())


if a == b and b == c:
     print(a*1000+10000)
else:
     if a == b:
          print(a*100+1000)
     elif b == c:
          print(b*100+1000)
     elif a == c:
          print(a*100+1000)
     else:
          d = [a, b, c]
          d.sort()
          print(d[2]*100)