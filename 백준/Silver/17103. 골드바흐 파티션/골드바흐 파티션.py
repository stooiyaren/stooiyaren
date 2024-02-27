import sys
input = sys.stdin.readline

def prime(n):
    number = list(range(n+1))
    for i in range(2,n+1):
        if number[i] == 0:
            continue
        for j in range(i*i,n+1,i):
            number[j] = 0
    return number

    # optimus = []
    # for i in number:
    #     if i != 0 and i != 1:
    #         optimus.append(i)
    # return optimus

num = prime(1000000)
num[1] = 0
T = int(input())
for tc in range(T):
    N = int(input())
    cnt = 0
    for i in range(len(num)):
        if N//2 < num[i]:
            break
        if num[N - num[i]]:
            cnt += 1
    print(cnt)