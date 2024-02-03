import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    A,B = input().split()
    A = list(A)
    B = list(B)

    for i in A:
        if i in B:
            B.remove(i)
        else:
            break
    if len(B) == 0:
        print('Possible')
    else:
        print('Impossible')