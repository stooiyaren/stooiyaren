n = int(input())
score = [0] * n
for i in range(n):
    score[i] = int(input())
score.sort()

b = n*0.15
if b - int(b) >= 0.5:
    p = int(b)+1
else:
    p = int(b)

a = score[p:n-p]
if a:
    c = sum(a)/len(a)
    if c - int(c) >= 0.5:
        print(int(c)+1)
    else:
        print(int(c))
else:
    print(0)