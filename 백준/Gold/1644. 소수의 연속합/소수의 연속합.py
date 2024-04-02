N = int(input())

num = [1] *(N+1)
prime = []

for i in range(2,N+1): # 1은 소수가 아니다
    if num[i] == 1:
        prime.append(i)
        for j in range(i*i,N+1,i): # 제곱수 이전까지는 이미 계산되어있음
            num[j] = 0
# 에라스토 체 완성
l = len(prime)
cnt = 0
for i in range(l):
    total = 0
    for j in range(i,l):
        total += prime[j]

        if total == N:
            cnt += 1
            break
        elif total > N:
            break

print(cnt)