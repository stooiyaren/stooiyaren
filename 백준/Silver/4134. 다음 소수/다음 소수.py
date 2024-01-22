import sys
import math

def sosu(n):
    for i in range(3,int(math.sqrt(n)) + 1,2):
        if n%i==0:
            return False
        else:
            pass
    return True
    

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    while True:
        if n == 0 or n ==1 or n==2:
            n = 2
            break
        if n%2==0:
            n += 1
        elif sosu(n) == True:
            break
        else:
            n += 2
    print(n)