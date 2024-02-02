N = list(map(int, input().split()))
N = [x**2 for x in N]
print(sum(N)%10)