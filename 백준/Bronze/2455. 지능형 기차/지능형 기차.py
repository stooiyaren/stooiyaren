best = 0
left = 0
for i in range(4):
    out, come = map(int, input().split())
    left = left + come - out
    if best < left:
        best = left
print(best)