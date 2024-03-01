w, h = map(int,input().split())
x, y = map(int,input().split())
t = int(input())

dx = t % (2*w)
dy = t % (2*h)

if dx <= w - x:
    x = x + dx
elif dx <= 2*w - x:
    x = 2*w - x - dx
else:
    x = x + dx - 2*w

if dy <= h - y:
    y = y + dy
elif dy <= 2*h - y:
    y = 2*h - y - dy
else:
    y = y + dy - 2*h

print(x,y)