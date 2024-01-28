import sys
input = sys.stdin.readline

N = int(input())
count = 0
for i in range(N):
    m = int(input())
    count += m-1
print(count+1)