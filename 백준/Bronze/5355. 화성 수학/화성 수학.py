T = int(input())
for i in range(T):
    m = list(input().split())
    cnt = float(m[0])
    for j in range(1,len(m)):
        if m[j] == '@':
            cnt *=3
        elif m[j] =='%':
            cnt += 5
        elif m[j] == '#':
            cnt -=7
    print("{:.2f}".format(cnt))