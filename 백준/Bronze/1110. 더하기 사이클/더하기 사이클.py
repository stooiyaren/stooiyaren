def change(n):
    if n < 10:
        return n*10 + n
    else:
        return n%10*10 + (n%10 + n//10)%10

N = int(input())
cnt = 1
n = -1
n = change(N)
while True:
    if N == n:
        break
    n = change(n)
    cnt += 1
print(cnt)