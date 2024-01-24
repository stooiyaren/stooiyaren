A, I = map(int, input().split())
if A == 1 or I==1:
    print(A*I)
else:
    print(A*(I-1)+1)