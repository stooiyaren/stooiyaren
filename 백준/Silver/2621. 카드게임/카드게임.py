def game(card):
    for i in range(4):
        if card[i+1][0]-card[i][0] != 1:
            break
        if card[i+1][1] != card[i][1]:
            break
    else:
        return 900 + card[4][0] # 1번 규칙
    
    if card[0][0] == card[1][0] and card[1][0] == card[2][0] and card[2][0] == card[3][0] or card[1][0] == card[2][0] and card[2][0] == card[3][0] and card[3][0] == card[4][0]:
        return 800 + card[2][0] # 2번 규칙
    else:
        if (len(set(nu[:3])) == 1 and len(set(nu[3:])) == 1):
            return 700 + nu[0]*10 + nu[-1]        
        elif (len(set(nu[:2])) == 1 and len(set(nu[2:])) == 1):
            return 700 + nu[-1] *10 + nu[0] # 3번 규칙
        else:
            for j in range(4):
                if co[j+1] != co[j]:
                    break
            else:
                return 600 + nu[-1] # 4번 규칙
            
            for i in range(4):
                if nu[i+1]-nu[i] != 1:
                    break
            else:
                return 500 + nu[-1] # 5번 규칙
            
            for i in range(1,10):
                if nu.count(i) == 3:
                    return 400 + i # 6번 규칙
            a = 0
            cnt = 0
            for i in range(1,10):
                if nu.count(i) == 2:
                    if cnt ==1:
                        return 300 + i *10 + a # 7번 규칙
                    else:
                        cnt += 1
                        a = i
            
            if cnt == 1:
                return 200 + a # 8번 규칙
            
            return 100 + nu[-1] # 9번 규칙
                        
                        

card = [0]*5
co = [0]*5
nu = [0]*5
for i in range(5):
    color, number = map(str,input().split())
    number = int(number)
    card[i] = [number,color]
    co[i] = color
    nu[i] = number 
card.sort()
nu.sort()
print(game(card))