N = int(input())
count = 0
for i in range(N):
    a = list(input())
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            continue
        elif a[j] in a[j+1:]:
            count +=1
            break
print(N-count)