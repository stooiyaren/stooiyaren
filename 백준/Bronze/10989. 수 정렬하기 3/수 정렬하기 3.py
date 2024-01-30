import sys
input = sys.stdin.readline
N = int(input())
increase = [0]*10001
for i in range(N):
    increase[int(input())] += 1

for i in range(1, 10001):
    for j in range(increase[i]):
        print(i)