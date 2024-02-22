number = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

def check(n): # 홀수자리합 *3 + 짝수 자리 합 이 10의 배수
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        if i % 2 == 0:
            cnt1 += n[i]
        else:
            cnt2 += n[i]
    ans = (cnt2 + cnt1*3) % 10
    if ans:
        return False
    else:
        return True
            

def deci(n):
    num = []
    for i in range(8):
        num.append(number[''.join(map(str, n[7*i:7*i+7]))])
    return num

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    receipt = [list(map(int,input())) for _ in range(N)]

    for i in range(N):
        if 1 in receipt[i]:
            height = i
            break

    for i in range(M-1,-1,-1):
        if receipt[height][i] == 1:
            end = i
            break

    bacord = receipt[height][end-55:end+1]

    if check(deci(bacord)):
        print(f'#{tc}', sum(deci(bacord)))
    else:
        print(f'#{tc}', 0)