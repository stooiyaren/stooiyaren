from collections import deque
for i in range(10):
    sol = False
    n = int(input())
    password = deque(map(int,input().split()))
    while True:
        for i in range(1,6):
            password[0] -= i
            password.rotate(-1)
            if password[-1] <= 0:
                password[-1] = 0
                sol = True
                break
        if sol:
            break
    print(f'#{n}', *password)
