import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    m = list(map(int, input().split()))
    print(sum(m))