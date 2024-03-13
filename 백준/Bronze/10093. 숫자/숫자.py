A, B = map(int,input().split())
if A == B:
    print(0)
else:
    if A>B:
        A,B = B,A
    print(B-A-1)
    for i in range(A+1,B):
        print(i,end=' ')