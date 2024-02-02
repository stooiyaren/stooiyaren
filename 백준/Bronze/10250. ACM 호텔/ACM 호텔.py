import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())

    if N%H ==0:
        floor = str(H)
        room = N//H
    else:
        floor = str(N%H)
        room = 1+N//H
    if room > 9:
        print(floor+str(room))
    else:
        print(floor+'0' + str(room)) 