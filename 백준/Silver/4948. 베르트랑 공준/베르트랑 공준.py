import sys
input = sys.stdin.readline


def prime(n):
    if n == 1:
        return 1
    number = list(range(2*n+1))
    for i in range(2,2*n+1):
        if number[i] == 0:
            continue
        for j in range(i*i,2*n+1,i):
            number[j] = 0
    ans = 0
    for i in number:
        if i != 0 and n < i:
            ans += 1
    return ans
    
n = int(input())

while n:

    print(prime(n))

    n = int(input())