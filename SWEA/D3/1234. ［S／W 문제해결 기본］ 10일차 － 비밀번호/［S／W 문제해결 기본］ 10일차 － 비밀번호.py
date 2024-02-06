for tc in range(1,11):
    N, S = input().split()
    cnt = 0
    while True:
        if cnt == len(S) - 2:
            break
        if S[cnt] == S[cnt+1]:
            S = S[:cnt] + S[cnt+2:]
            if cnt != 0:
                cnt -= 1
        else:
            cnt += 1
    if S[-2] == S[-1]:
        S = S[:-2]
    print(f'#{tc} {S}')