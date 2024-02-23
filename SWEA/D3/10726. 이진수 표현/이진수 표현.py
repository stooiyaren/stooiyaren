T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    key = 2**N-1
    if M & key == key:
        print(f'#{tc} ON')
    else:
        print(f'#{tc} OFF')