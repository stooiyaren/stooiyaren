def postorder(n):
    if n:
        postorder(left[n])
        postorder(right[n])
        if left[n] and right[n]:
            if par[n] == '+':
                par[n] = par[left[n]] + par[right[n]]
            elif par[n] == '-':
                par[n] = par[left[n]] - par[right[n]]
            elif par[n] == '*':
                par[n] = par[left[n]] * par[right[n]]
            elif par[n] == '/':
                par[n] = par[left[n]] // par[right[n]]

for tc in range(1,11):
    N = int(input())

    par = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N):
        order = list(input().split())
        p = int(order[0])
        if order[1].isdecimal():
            par[p] = int(order[1])
        else:
            par[p] = order[1]
        if len(order) >= 3:
            left[p] = int(order[2])
        if len(order) == 4:
            right[p] = int(order[3])

    postorder(1)
    print(f'#{tc}', par[1])