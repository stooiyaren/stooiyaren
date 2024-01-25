import sys
input = sys.stdin.readline

M, F = map(int, input().split())
while M != 0 and F != 0:
    print(M+F)
    M, F = map(int, input().split())