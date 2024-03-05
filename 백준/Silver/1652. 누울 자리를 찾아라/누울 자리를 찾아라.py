N = int(input())

room = [list(input()) for _ in range(N)]

rans = 0
for i in room:
    rcnt = 0
    for j in i:
        if j == 'X':
            if rcnt >1:
                rans +=1
            rcnt = 0
        else:
            rcnt += 1
    if rcnt > 1:
        rans += 1
    
room = list(map(list,zip(*room)))

cans = 0
for i in room:
    ccnt = 0
    for j in i:
        if j == 'X':
            if ccnt >1:
                cans +=1
            ccnt = 0
        else:
            ccnt += 1
    if ccnt > 1:
        cans += 1

print(rans, cans)