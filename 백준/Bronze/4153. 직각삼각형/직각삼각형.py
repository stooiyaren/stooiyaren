while True:
    A, B, C = map(int,input().split())
    if A==B and B == C and C == 0:
        break
    A_square = A**2
    B_square = B**2
    C_square = C**2
    hap = A_square + B_square + C_square
    if max(A_square, B_square, C_square) == hap - max(A_square, B_square, C_square):
        print('right')
    else:
        print('wrong')