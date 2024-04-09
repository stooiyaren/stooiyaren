N = int(input())
person = list(map(int,input().split()))
B, C = map(int,input().split())
ans = 0

for i in person:
    i -= B
    if i > 0:
        if i %C:
            ans += i//C + 2
        else:
            ans += i//C + 1
    else:
        ans += 1
print(ans)