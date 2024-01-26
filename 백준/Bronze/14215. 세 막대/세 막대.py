A, B, C = map(int, input().split())
if max(A, B, C) < (A + B + C) - max(A, B, C):
    print(A+B+C)
else:
    print(((A + B + C) - max(A, B, C))*2-1)