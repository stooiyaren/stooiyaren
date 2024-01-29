N = int(input())
for i in range(N):
    if i %2 == 0:
        print('* '*(N-1)+'*')
    elif i %2 ==1:
        print(' *'*N)