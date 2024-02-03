import sys
import math
input = sys.stdin.readline

num = [0]*10
N = list(map(int,input().strip()))
for i in N:
    num[i] += 1
num[6] = math.ceil((num[6]+num[9])/2)
num[9] = num[6]

print(max(num))