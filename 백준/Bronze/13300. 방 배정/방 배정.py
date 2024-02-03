import sys
import math
input = sys.stdin.readline

N,K = map(int,input().split())
woman =[0]*7
man =[0]*7
room = 0

for i in range(N):
    S, Y = map(int, input().split())
    if S == 1:
        man[Y] += 1
    else:
        woman[Y] += 1

for i in range(7):
    room += math.ceil(woman[i]/K)
    room += math.ceil(man[i]/K)
print(room)