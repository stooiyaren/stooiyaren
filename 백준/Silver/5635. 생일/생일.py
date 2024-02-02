n = int(input())

for i in range(n):
    name, dd, mm, yy = input().split()
    dd, mm, yy = map(int, [dd, mm, yy])

    if i == 0:
        o_y = yy
        o_m = mm
        o_d = dd
        y_y = yy
        y_m = mm
        y_d = dd
        youngest = name
        oldest = name
    else:
        if o_y > yy or (o_y == yy and (o_m > mm or (o_m == mm and o_d > dd))):
            o_y = yy
            o_m = mm
            o_d = dd
            oldest = name

        if y_y < yy or (y_y == yy and (y_m < mm or (y_m == mm and y_d < dd))):
            y_y = yy
            y_m = mm
            y_d = dd
            youngest = name

print(youngest)
print(oldest)