import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    y = [0]*9
    k = [0]*9
    for j in range(9):
        y[j], k[j] = map(int, input().split())
    if sum(y) > sum(k):
        print('Yonsei')
    elif sum(y) == sum(k):
        print('Draw')
    else:
        print('Korea')