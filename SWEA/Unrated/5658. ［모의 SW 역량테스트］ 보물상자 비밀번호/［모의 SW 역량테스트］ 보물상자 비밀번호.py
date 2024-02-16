def numbering(n):
    number = 0
    cnt = 0
    for i in range(len(n)):
        cnt += 1
        if n[i] in '1234567890':
            number += int(n[i])*16**(len(n) - i-1)
        else:
            alpabet = ['A','B','C','D','E','F']
            number += (alpabet.index(n[i])+ 10)*16**(len(n) - i -1)
    return number

from collections import deque

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    s = deque(input())
    tall = N//4
    password = []
    for i in range(tall):
        for j in range(4):
            cnt = ''
            for k in range(tall):
                cnt += s[(tall*j)+k]
            cnt = numbering(cnt)            
            password.append(cnt)
        s.rotate(1)
    password = list(sorted(set(password)))
    print(f'#{tc}', password[-K])