import sys
input = sys.stdin.readline


N= int(input())
s = 666
n = 1
cnt = 0
while True:
    n = str(n)
    if '666' in n:
        cnt += 1
        if cnt == N:
            break
    n = int(n)
    n += 1
print(n)