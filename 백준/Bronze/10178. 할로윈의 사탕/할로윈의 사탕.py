T = int(input())
for i in range(0, T):
    c, v = map(int,input().split())
    print(f'You get {c//v} piece(s) and your dad gets {c%v} piece(s).')