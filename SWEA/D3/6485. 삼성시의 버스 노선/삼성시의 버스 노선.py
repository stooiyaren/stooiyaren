T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bus_stop = [0] *5001 
    for i in range(N):
        bus = list(map(int,input().split()))
        for j in range(bus[0],bus[1]+1):
            bus_stop[j] += 1

    P = int(input())
    print(f'#{tc}',end = ' ')
    for i in range(P):
        print(bus_stop[int(input())], end = ' ')
    print()