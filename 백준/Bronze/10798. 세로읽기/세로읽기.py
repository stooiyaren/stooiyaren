a=[]
b=[]
for i in range(5):
    a.append(input())
for i in range(5):
    b.append(list(a[i]))
# mx = 0
# for i in range(5):
#    mx = max(mx, len(b[i]))
length = max(map(len, b))
for i in range(5):
    diff = length - len(b[i])
    b[i] = b[i] + [''] * diff

# zip(b[0], b[1], b[2], ...)
c =list(zip(*b))

for i in range(length):
    for j in range(5):
        print(c[i][j],sep='',end='')
