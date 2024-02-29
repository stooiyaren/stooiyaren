N = int(input())
number = list(map(int,input().split()))

if N == 1:
    print(1)
else:
    num = [[number[0],1]]
    best = 0
    for i in range(1,N):
        if number[i] == number[i-1]:
            num[-1][1] += 1
        else:
            num.append([number[i],1])
    if len(num) == 1:
        print(num[0][1])
    else:
        cnt = 0
        if num[1][0] > num[0][0]:
            crease = 1
        else:
            crease = -1
        cnt += num[0][1]

        for i in range(1,len(num)):
            if num[i-1][0] < num[i][0]:
                if crease == 1:
                    cnt += num[i][1]
                else:
                    crease = 1
                    if cnt > best:
                        best = cnt
                    cnt = num[i-1][1] + num[i][1]

            else:
                if crease == -1:
                    cnt += num[i][1]
                else:
                    crease = -1
                    if cnt > best:
                        best = cnt
                    cnt = num[i-1][1] + num[i][1]
        if cnt > best:
            best = cnt
    
        print(best)