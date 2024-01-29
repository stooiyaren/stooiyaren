T = int(input())
for i in range(1, T+1):
    dice = list(map(int,input().split()))
    print(f'Case {i}: {sum(dice)}')