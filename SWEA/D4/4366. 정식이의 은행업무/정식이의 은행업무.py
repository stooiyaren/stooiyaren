
T = int(input())
for tc in range(1,T+1):
    bi = list(map(int,input()))
    tri = list(map(int,input()))

    binum = 0
    bi.reverse()
    for i in range(len(bi)-1,-1,-1):
        binum += 2**i * bi[i]
    check = binum

    bilist = []
    for i in range(len(bi)-1,-1,-1):
        if bi[i] == 1:
            binum -= 2**i * bi[i]
        else:
            binum += 2**i
        bilist.append(binum)
        binum = check

    trinum = 0
    tri.reverse()
    for i in range(len(tri)-1,-1,-1):
        trinum += 3**i * tri[i]
    ceck = trinum

    
    for i in range(len(tri)-1,-1,-1):
        trinum -= tri[i] * 3**i

        if tri[i] == 2:
            if trinum + 3**i in bilist:
                ans = trinum + 3**i
                break
            elif trinum in bilist:
                ans = trinum
                break
        elif tri[i] == 1:
            if trinum + 2*3**i in bilist:
                ans = trinum + 2*3**i
                break
            elif trinum in bilist:
                ans = trinum
                break
        elif tri[i] == 0:
            if trinum + 2*3**i in bilist:
                ans = trinum + 2*3**i
                break
            elif trinum + 3**i in bilist:
                ans = trinum + 3**i
                break
        trinum = ceck
    print(f'#{tc}', ans)