letter = "MOBIS"
word = str(input().strip())

ans = 1

for i in letter:
    for j in word:
        if i == j:
            break
    else:
        ans = 0
        break

if ans:
    print('YES')
else:
    print('NO')