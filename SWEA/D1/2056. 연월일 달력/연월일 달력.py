T = int(input())
for i in range(1,T+1):
    sett = str(input())
    ymd = int(sett)
    year = ymd//10000
    month = (ymd//100)%100
    date = ymd%100
    count = 0
    y = sett[0:4]
    m = sett[4:6]
    d = sett[6:]
    
    if month < 1 or date < 1:
        count += 1

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if date > 31:
            count += 1
    if month == 2:
        if date >28:
            count += 1
    if month == 4 or month == 6 or month == 9 or month == 11:
        if date >30:
            count += 1

    if count ==0:
        print(f"#{i} {y}/{m}/{d}")
    else:
        print(f"#{i} -1")