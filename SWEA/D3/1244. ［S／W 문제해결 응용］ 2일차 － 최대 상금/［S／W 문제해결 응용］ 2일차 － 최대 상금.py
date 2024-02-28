T = int(input())
for tc in range(1,T+1):
    number, change = input().split()
    change = int(change)
    number = list(number)
    n = len(number)
    a = list(map(int,number))
    best = sorted(a, reverse = True)

    history = set()

    mx = 0
    def dfs(change):
        global mx

        if (change, int(''.join(number))) in history:
            return

        history.add((change, int(''.join(number))))
        if best == number:
            if n%2 == 0:
                mx = max(temp,mx)
            else:
                number[-2], number[-1] = number[-1], number[-2]
            return

        if change == 0:
            temp = int(''.join(number))
            if mx < temp:
                mx = temp
            return

        for i in range(n-1):
            for j in range(i+1,n):
                number[i], number[j] = number[j], number[i]
                dfs(change-1)
                number[i], number[j] = number[j], number[i]
    dfs(change)
    print(f'#{tc}', mx)