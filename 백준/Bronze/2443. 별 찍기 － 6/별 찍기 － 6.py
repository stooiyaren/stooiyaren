N = int(input())
b = N
c = 0
for i in range(N,0,-1):
    print(' '*c+'*'*(2*i-1))
    c +=1