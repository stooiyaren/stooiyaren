for tc in range(1, 11):
    N = int(input())
    n = list(input().split('+'))
    for i in range(len(n)):
        if len(n[i]) > 1:
            cnt = 1
            factors = list(map(int, n[i].split('*')))
            for num in factors:
                cnt *= num
            n[i] = cnt
        else:
            n[i] = int(n[i])

    print(f'#{tc}', sum(n))