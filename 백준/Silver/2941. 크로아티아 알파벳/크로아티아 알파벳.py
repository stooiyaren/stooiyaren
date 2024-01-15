cr = ['c=','c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

word = str(input())
wl = len(word)

for i in range(8):
    if i == 2:
        count += 2 * word.count(cr[2])
    elif i == 7:
        count += word.count(cr[7]) - word.count(cr[2])
    else:
        count += word.count(cr[i])

print(wl-count)