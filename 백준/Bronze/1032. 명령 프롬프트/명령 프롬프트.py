T = int(input())
letter1 = list(input())
dir_letter = letter1.copy()
for i in range(T-1):
    letters = list(str(input()))
    for j in range(len(letter1)):
        if dir_letter[j] != letters[j]:
               dir_letter[j] = '?'
print(*dir_letter,sep='')