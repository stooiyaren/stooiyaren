T = int(input())
for tc in range(1,T+1):
    N = int(input())
    card = list(map(str,input().split()))
    ans = []

    if N %2 == 1:
        partition = N//2 +1
    else:
        partition = N // 2
    
    for i in range(N//2):
        ans.append(card[i])
        ans.append(card[i + partition])

    if N %2 == 1:
        print(f'#{tc}', *ans,card[N//2])
    else:
        print(f'#{tc}', *ans)