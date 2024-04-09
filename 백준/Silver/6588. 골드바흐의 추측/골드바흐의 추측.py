import sys
input = sys.stdin.readline

N = 1000000
check = [True]*N
check[0] = check[1] = False

n = int(N**0.5)
for i in range(2,n+1):
    if check[i]:
        for j in range(i*i,N,i):
            check[j] = False

while True:
    p = int(input())

    if p == 0: # 0이면 종료
        break

    for i in range(3,p//2+1,2):
        if check[i] and check[p-i]:
            print(f'{p} = {i} + {p-i}')
            break