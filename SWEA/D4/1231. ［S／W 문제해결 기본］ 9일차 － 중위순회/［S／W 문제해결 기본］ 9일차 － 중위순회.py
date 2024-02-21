def inorder(T):
    if T:    
        inorder(left[T])
        print(par[T], end = '')
        inorder(right[T])
    else:
        return



for tc in range(1,11):
    N = int(input())

    par = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N):
        order = list(input().split())
        par[int(order[0])] = order[1]
        if len(order) == 3:
            left[int(order[0])] = int(order[2])
        if len(order) == 4:
            left[int(order[0])] = int(order[2])
            right[int(order[0])] = int(order[3])
    print(f'#{tc}', end = ' ')
    inorder(1)
    print()