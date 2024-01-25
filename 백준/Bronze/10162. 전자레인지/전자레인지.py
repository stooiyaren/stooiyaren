import sys
input = sys.stdin.readline

T = int(input())
A = T//300
B = T%300//60
C = T%300%60//10
if T != 300*A+60*B+10*C:
    print(-1)
else:
    print(A, B, C)