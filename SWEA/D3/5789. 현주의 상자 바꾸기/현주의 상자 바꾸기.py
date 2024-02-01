T = int(input())
for t in range(1, T + 1):
    N, Q = map(int, input().split())
    lst = [0] * (N + 1)
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L, R + 1):
            lst[j] = i
    lst.pop(0) 
    print(f'#{t}', *lst)