T = int(input())
for i in range(1,T+1):
    count = 0
    N = int(input())
    s = list(map(int, input().split()))[::-1]
    max_value = s[0]
    for j in range(N):
        if s[j] > max_value:
            max_value = s[j]
        else:
            count += max_value - s[j]
    print(f'#{i} {count}')