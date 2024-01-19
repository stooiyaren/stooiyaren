import sys
n1, n2 = map(int, sys.stdin.readline().split())
while n1 !=0 and n2 !=0:
    if n2 % n1 == 0:
        print('factor')
    elif n1 % n2 == 0:
        print('multiple')
    else:
        print('neither')
        
    n1, n2 = map(int, sys.stdin.readline().split())