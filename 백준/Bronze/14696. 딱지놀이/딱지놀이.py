def game(A,B):
    a = A[0]
    A = A[1:]
    A.sort()

    b = B[0]
    B = B[1:]
    B.sort()

    while A and B:
        aa = A.pop()
        bb = B.pop()
        if aa == bb:
            continue
        elif aa > bb:
            return 'A'
        else:
            return 'B'
    if A:
        return 'A'
    elif B:
        return 'B'
    else:
        return 'D'

N = int(input())
for i in range(N):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    print(game(A,B))
