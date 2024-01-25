import sys
input = sys.stdin.readline

N = int(input())
increase = []
for i in range(N):
    increase.append(int(input()))
increase.sort()
for i in range(N):
    print(increase[i])