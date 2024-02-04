T = int(input())
for tc in range(1,T+1):
    N = int(input())
    n = str(input())
    cnt = int(n[0])
    best = 0
    for i in range(1, N):
        if n[i] == '1':
            cnt += 1
            if cnt > best:
                best = cnt
        else:
            cnt = 0
    print(f'#{tc} {best}')