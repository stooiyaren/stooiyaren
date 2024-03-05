km = int(input())
garo = []
sero = []
als = 0
direction, length = map(int,input().split())
if direction >= 3:
    garo.append(length) # 실제론 세로임
    als = 1    
else:
    sero.append(length) # 실제론 가로임

for i in range(5):
    direction, length = map(int,input().split())
    if als == 1:
        if i%2==1:
            garo.append(length)
        else:
            sero.append(length)
    else:
        if i%2 ==1:
            sero.append(length)
        else:
            garo.append(length)
whole = max(garo)*max(sero)        
if als: # 세로시작
    if max(garo) == garo[0]:
        if max(sero) == sero[0]:
            print(km * (whole - garo[2]*sero[1]))
        #elif max(sero) == sero[1]:
         #   print(km * (whole - garo[2]*sero[2]))        
        elif max(sero) == sero[2]:
            print(km * (whole - garo[1]*sero[1]))
    elif max(garo) == garo[1]:
        if max(sero) == sero[0]:
            print(km * (whole - garo[2]*sero[2]))
        elif max(sero) == sero[1]:
            print(km * (whole - garo[0]*sero[2]))        
        #elif max(sero) == sero[2]:
         #   print(km * (whole - garo[0]*sero[0]))
    elif max(garo) == garo[2]:
        #if max(sero) == sero[0]:
         #   print(km * (whole - garo[0]*sero[2]))
        if max(sero) == sero[1]:
            print(km * (whole - garo[0]*sero[0]))        
        elif max(sero) == sero[2]:
            print(km * (whole - garo[1]*sero[0]))

else:
    if max(sero) == sero[0]:
        if max(garo) == garo[0]:
            print(km * (whole - garo[1]*sero[2]))
        #elif max(garo) == garo[1]:
        #    print(km * (whole - garo[2]*sero[2]))        
        elif max(garo) == garo[2]:
            print(km * (whole - garo[1]*sero[1]))
    elif max(sero) == sero[1]:
        if max(garo) == garo[0]:
            print(km * (whole - garo[2]*sero[2]))
        elif max(garo) == garo[1]:
            print(km * (whole - garo[2]*sero[0]))        
        #elif max(garo) == garo[2]:
        #    print(km * (whole - garo[0]*sero[0]))
    elif max(sero) == sero[2]:
        #if max(garo) == garo[0]:
         #   print(km * (whole - garo[2]*sero[0]))
        if max(garo) == garo[1]:
            print(km * (whole - garo[0]*sero[0]))        
        elif max(garo) == garo[2]:
            print(km * (whole - garo[0]*sero[1]))
