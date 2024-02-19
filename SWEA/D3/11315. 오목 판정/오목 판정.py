T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    omok = [input() for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            cnt1 = 0
            cnt2 = 0

            for k in range(5):
                if 0<= (i+k) < N and 0<= (j+k) < N and omok[i+k][j+k] == 'o':
                    cnt1 += 1

                if 0<=(i-k)<N and 0<=(j+k)<N and omok[i-k][j+k] == 'o':
                    cnt2 += 1
            if cnt1 == 5:
                ans = 1
                break
            if cnt2 == 5:
                ans = 1
                break

    for i in omok:
        if 'ooooo' in i:
            ans = 1
            break

    omok = list(map(list,zip(*omok)))
    
    for i in omok:
        i = ''.join(i)
        if 'ooooo' in i:
            ans = 1
            break

    if ans:
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')
