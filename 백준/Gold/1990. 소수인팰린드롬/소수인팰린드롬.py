import sys
input = sys.stdin.readline

M, N = map(int,input().split())
if M >= 9989900:
    print(-1)
else:
    number = list(range(9989900))
    prime = []
    for i in range(2,9989900):
        if number[i] == 0:
            continue
        for j in range(i*i,9989900,i):
            number[j] = 0
    for i in number:
        if i != 0 and i != 1 and M<=i and str(i) ==str(i)[::-1] and i <= N:
            print(i)
    print(-1)