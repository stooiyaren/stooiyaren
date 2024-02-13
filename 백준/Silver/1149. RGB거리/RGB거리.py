N = int(input())
color = list(map(int, input().split()))
price = [0,0,0]
for i in range(1,N):
    red, green, blue = map(int,input().split())
    
    price[0] = red + min(color[1],color[2])
    price[1] = green + min(color[0],color[2])
    price[2] = blue + min(color[0],color[1])
    color = price.copy()
print(min(price))