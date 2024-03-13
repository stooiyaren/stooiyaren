import math
N = int(input())
phone = list(map(int,input().split()))
Y = 0
M = 0
for i in phone:
    Y += (int(i/30)+1)*10
    M += (int(i/60)+1)*15

if Y > M:
    print('M', M)
elif M > Y:
    print('Y', Y)
else:
    print('Y','M', Y)