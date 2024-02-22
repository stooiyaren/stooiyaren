dwarf = [0]*9
for i in range(9):
    dwarf[i] = int(input())

tall = sum(dwarf) - 100

for i in range(8):
    for j in range(i+1,9):
        if dwarf[i] + dwarf[j] == tall:
            del dwarf[i]
            del dwarf[j-1]
            break
    if len(dwarf) != 9:
        break
dwarf.sort()
for i in range(7):
    print(dwarf[i])