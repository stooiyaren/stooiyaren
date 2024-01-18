X = int(input())
n = 1
while n!=0:
    if X == 1:
        row = 1
        line = 1
        break
    if n*(n+1) < 2*X <= (n+1)*(n+2):
        x = int((n+1)*(n+2)/2-X)
        if n%2 == 0:
            row = n+1 - x
            line = 1 + x
            break
        elif n%2 == 1:
            row = 1 + x
            line = n+1 - x
            break
    n += 1
print(f'{line}/{row}')
