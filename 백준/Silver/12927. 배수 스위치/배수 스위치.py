switch = list(input())
switch = ['N']+switch
cnt = 0
for i in range(1,len(switch)):
    if switch[i] == 'N':
        continue
    else:
        for j in range(i,len(switch),i):
            if switch[j] == 'Y':
                switch[j] = 'N'
            else:
                switch[j] = 'Y'
        cnt += 1

print(cnt)