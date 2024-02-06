num = [1,2,3,4,5,6,7,8,9]
T = int(input())
for tc in range(1,T+1):
    doku =[list(map(int,input().split())) for _ in range(9)]
    s = 1

    for i in range(9):
        if num != sorted(doku[i]):
            s = 0

    for i in range(0,9,3):
        for j in range(0,9,3):
            d =[]
            for p in range(3):
                for q in range(3):
                    d.append(doku[i+p][j+q])
            d.sort()
            if num != d:
                s = 0

    doku = [list(t_row) for t_row in zip(*doku)]
    for i in doku:
        i.sort()
        if num != i:
            s = 0
    print(f'#{tc} {s}')