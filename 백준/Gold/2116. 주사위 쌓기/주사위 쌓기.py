import copy

def encount(n):
    if n == 0:
        return 5
    elif n == 1:
        return 3
    elif n == 2:
        return 4
    elif n == 3:
        return 1
    elif n == 4:
        return 2
    elif n == 5:
        return 0
    
mx = 0

N = int(input())
dice = []
for i in range(N):
    d = list(map(int,input().split()))
    dice.append(d)

for i in range(6):
    dicee = copy.deepcopy(dice)
    top = dicee[0][i]
    bot = dicee[0][encount(i)]
    dicee[0].remove(top)
    dicee[0].remove(bot)
    for j in range(1,N):
        top = bot
        bot = dicee[j][encount(dicee[j].index(top))]
        dicee[j].remove(top)
        dicee[j].remove(bot)
    sum = 0
    for p in range(N):
        sum += max(dicee[p])

    if mx < sum:
        mx = sum
print(mx)