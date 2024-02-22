T = int(input())
for tc in range(1, T+1):
    daily, monthly, three, yearly = map(int,input().split())
    plan = [0] + list(map(int,input().split())) + [0,0]

    for i in range(1,13):
        plan[i] *= daily

    for i in range(1,13):
        if monthly < plan[i]:
            plan[i] = monthly

    d = [0] * 13
    d[1] = plan[1]
    d[2] = plan[1] + plan[2]
    d[3] = min((plan[1] + plan[2] + plan[3]),three)
    d[4] = min(d[3] + plan[4],plan[1] + three)
    d[5] = min(d[4] + plan[5], plan[1]+plan[2] + three)
    for i in range(6,13):
        d[i] = min(d[i-1]+plan[i],d[i-3]+three)

    if d[12] < yearly:
        print(f'#{tc}', d[12])
    else:
        print(f'#{tc}', yearly)