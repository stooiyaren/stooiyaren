import sys
input = sys.stdin.readline

T = int(input())
winner = ''
amount = 0
for i in range(T):
    N = int(input())
    for j in range(N):
        S, L = input().split()
        L = int(L)
        if  amount < L:
            winner = S
            amount = L
    print(winner)