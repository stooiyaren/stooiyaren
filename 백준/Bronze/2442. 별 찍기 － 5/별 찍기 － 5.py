N = int(input())
b = N
c = 1
for i in range(1,N+1):
    b -= 1
    print(' '*b+'*'*(2*i-1))