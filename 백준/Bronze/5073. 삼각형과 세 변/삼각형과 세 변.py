A, B, C = map(int, input().split())

while A != 0 and B != 0 and C != 0:
    if max(A, B, C) >= (A + B + C) - max(A, B, C):
        print('Invalid')
    else:
        if A == B and B == C:
            print('Equilateral')
        elif A == B or B == C or C == A or A == C:
            print('Isosceles')
        elif A != B and B != C:
            print('Scalene')

    A, B, C = map(int, input().split())