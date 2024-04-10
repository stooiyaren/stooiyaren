T = int(input())
for tc in range(1, T+1):
    t = int(input())
    clothes = {}

    for _ in range(t):
        cloth, part = map(str, input().split())
        
        if part in clothes:
            clothes[part].append(cloth)
        else:
            clothes[part] = [cloth]

    ans = 1

    for i in clothes.keys():
        ans *= (len(clothes[i]) + 1)

    ans -= 1
    print(ans)