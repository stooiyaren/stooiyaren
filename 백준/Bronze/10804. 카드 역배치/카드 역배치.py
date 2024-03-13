def change(a,b):
    origin = card[a:b+1]
    cnt = 0
    for i in range(b,a-1,-1):
        card[i] = origin[cnt]
        cnt += 1
    

card = list(range(21))

for _ in range(10):
    A,B = map(int,input().split())
    change(A,B)
card.pop(0)
print(*card)