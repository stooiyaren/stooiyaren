T = int(input())
for i in range(1,T+1):
    a = list(map(int, input().split()))
    a.sort()
    print(f"#{i} {a[9]}")