import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
dogam = {}
dogam_tag = {}
for i in range(1,N+1):
    m = input().rstrip()
    dogam[i] = m
    dogam_tag[m] = i
for j in  range(M):
    n = input().rstrip()
    if n.isdecimal():
        print(dogam[int(n)])
    else:
        print(dogam_tag[n])