a = input()
b = input()
a1 = len(a)
b1 = len(b)
pas = 0
cnt = 0
for i in range(a1-b1+1):
    if pas:
        pas -= 1
    else:
        for j in range(b1):
            if a[i+j] != b[j]:
                break
        else:
            pas = b1-1
            cnt += 1
print(cnt)