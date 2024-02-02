b = 0
c = 0

for k in range(1, 10):
    d = int(input())

    if d > b:
        b = d
        c = k

print(b)
print(c)