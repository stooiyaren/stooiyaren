import sys
input = sys.stdin.readline

A = list(input().strip())
B = list(input().strip())
cnt = 0
for i in A:
    if i in B:
        cnt += 1
        B.remove(i)
print(len(A) +len(B) -cnt)