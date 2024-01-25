import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    result = input()
    count = 0
    score = 0
    if result[0] == 'O':
        count = 1
        score = 1
    for j in range(1,len(result)):
        if result[j-1]=='O' and result[j]=='O':
            count +=1
            score += count
        elif result[j-1]=='O' and result[j]=='X':
            count = 0
        elif result[j-1]=='X' and result[j]=='O':
            count += 1
            score += count
    print(score)