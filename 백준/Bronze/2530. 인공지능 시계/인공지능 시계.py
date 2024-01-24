A, B, C = map(int, input().split())
D = int(input())

second = A*3600 + B*60 + C + D
A = second //3600
B = (second -A*3600)//60
C = (second -A*3600 - B*60)
if A >=24:
    A %= 24
print(A,B,C)