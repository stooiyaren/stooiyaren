word = str(input().upper())
wl = len(word)
alphabet = [0]*26
for i in range(wl):
    alphabet[ord(word[i]) - 65] += 1

alco = alphabet.copy()
alphabet.sort()
if alphabet[25] == alphabet[24]:
    print('?')
else:
    for i in range(26):
        if alco[i] == alphabet[25]:
            print(chr(i+65))