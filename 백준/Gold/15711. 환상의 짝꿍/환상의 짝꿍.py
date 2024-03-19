n = 4*(10**12)
n = int(n**0.5)
number = [1]*(n+1)
prime = []
number[1] = 0
for i in range(2,n+1):
    if number[i] == 1:
        prime.append(i)
        for j in range(i*i,n+1,i):
            number[j] = 0

T = int(input())
for tc in range(T):
    a, b = map(int,input().split())
    num = a+b
    if num %2 == 0:
        if num ==2:
            print('NO')
        else:
            print('YES')
    else:
        if num > n:
            for i in prime:
                if not (num-2) % i: # 모든 소수로 나누었을 때 나머지가 없다면 .... 나누어 떨어진다면
                    print('NO') # 소수가 아닙니다.
                    break
            else: 
                print('YES') # 모든 i에 나머지가 0이 아니라면 소수이므로 for의 else문에 오게됩니다.
        else:
            if number[num-2]:
                print('YES')
            else:
                print('NO')