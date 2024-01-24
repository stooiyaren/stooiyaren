import sys
S = int(sys.stdin.readline())
n = 1
while 2*S >= (n+1)*(n+2): 
    n +=1
print(n)