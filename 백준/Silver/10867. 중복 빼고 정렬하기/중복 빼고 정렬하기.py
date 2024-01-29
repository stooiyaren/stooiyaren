import sys
input = sys.stdin.readline

N = int(input())
m = list(map(int,input().split()))
m = sorted(list(set(m)))
print(*m)