import sys
input = sys.stdin.readline

def ad(x):
    S.add(x)

def remo(x):
    if x in S:
        S.remove(x)

def ch(x):
    if x in S:
        return 1
    return 0

def to(x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def al():
    global S
    global A
    S = set(range(1,21))

def em():
    global S
    S = set()
S = set()
M = int(input())
for _ in range(M):
    order= list(input().split())

    if order[0] =='add':
        ad(int(order[1]))
    if order[0] == 'remove':
        remo(int(order[1]))
    if order[0] == 'check':
        print(ch(int(order[1])))
    if order[0] == 'toggle':
        to(int(order[1]))
    if order[0] == 'all':
        al()
    if order[0] == 'empty':
        em()