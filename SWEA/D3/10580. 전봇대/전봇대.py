T = int(input())
for tc in range(1,T+1):
    N = int(input())

    first =[]
    second = []
    cnt = 0

    for i in range(N):
        a,b = map(int,input().split())

        for j in range(len(first)):
            if a < first[j] and b > second[j]:
                cnt += 1

            elif a > first[j] and b < second[j]:
                cnt += 1

        first.append(a)
        second.append(b)
    print(f'#{tc} {cnt}')