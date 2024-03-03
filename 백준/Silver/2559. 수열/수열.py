N, K = map(int,input().split())
num = list(map(int,input().split()))
first = 0
second = K
cnt = sum(num[0:K])
mx = cnt
for _ in range(N-K):    
    cnt += num[second] - num[first]
    if cnt > mx:
        mx = cnt
    first += 1
    second += 1
print(mx)