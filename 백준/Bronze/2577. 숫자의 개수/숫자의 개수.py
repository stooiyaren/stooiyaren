import sys
input = sys.stdin.readline

A =int(input())
B =int(input())
C =int(input())

hap = str(A*B*C)
hap_lst = list(hap)
for i in range(10):
    print(hap_lst.count(str(i)))