import sys
input = sys.stdin.readline

n = int(input())
ai = list(map(int,input().split()))
x = int(input())
cnt = 0
ai.sort()

a = 0
b = n - 1

while a < b:
    if ai[a] + ai[b] >x:
        b -= 1

    elif ai[a] + ai[b] == x:
        cnt += 1
        a += 1
        b -= 1
    elif ai[a] + ai[b] < x:
        a += 1
print(cnt)