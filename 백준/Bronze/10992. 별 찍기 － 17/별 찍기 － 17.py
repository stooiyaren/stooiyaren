N = int(input())
print(' '*(N-1)+'*')
for i in range(N-2):
    print(' '*(N-2-i) + '*'+' '*(2*i+1)+'*')
if N != 1:
    print('*'*(2*N-1))