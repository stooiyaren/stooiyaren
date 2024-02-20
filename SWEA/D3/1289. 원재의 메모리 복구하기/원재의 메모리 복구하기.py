T = int(input())
for tc in range(1,T+1):
    n = str(input())
    start = 1
    cnt = 0
    
    for i in n:
        if start == 1 and i == '1':
            start *= -1
            cnt += 1
        elif start == -1 and i == '0':
            start *= -1
            cnt += 1

    print(f'#{tc}', cnt)
