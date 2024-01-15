words = list(str(input()))
words_length = len(words)
rewords = []
for i in range(words_length):
    words_length -= 1
    rewords.append(words[words_length])
if words == rewords:
    print('1')
else:
    print('0')