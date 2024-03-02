def bingo1():
    a = 0
    for i in range(5):
        for j in range(5):
            if i == j and ironwater[i][j] == 0:
                a += 1
    if a == 5:
        return 1
    else:
        return 0
    
def bingo2():
    b = 0
    for i in range(5):
        for j in range(5):
            if i + j == 4 and ironwater[i][j] == 0:
                b += 1
    if b == 5:
        return 1
    else:
        return 0

def bingo3():
    c = 0
    for i in ironwater:
        if i == [0]*5:
            c += 1
    return c

def bingo4():
    d = 0
    ironwaters = list(map(list,zip(*ironwater)))
    for i in ironwaters:
        if i == [0]*5:
            d += 1
    return d

ironwater = [list(map(int,input().split())) for _ in range(5)]
cnt = 0
check = 0
search = 0
for i in range(5):
    teacher = list(map(int,input().split()))
    for j in range(5):

        search = 0
        for p in range(5):
            for q in range(5):
                if ironwater[p][q] == teacher[j]:
                    ironwater[p][q] = 0
                    cnt += 1
                    search = 1
                    break
            if search:
                break

        ans = 0
        ans += bingo1()+ bingo2() + bingo3() + bingo4()        
        if ans >= 3:
            check = 1
            break
    if check:
        break
print(cnt)