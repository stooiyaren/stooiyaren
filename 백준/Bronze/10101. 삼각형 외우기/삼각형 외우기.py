A = int(input())
B = int(input())
C = int(input())
if A+B+C != 180:
    print('Error')
else:
    if A == B and B ==C:
        print('Equilateral')
    elif A == B or B == C or C == A:
        print('Isosceles')
    elif A != B and B != C:
        print('Scalene')