def check(a,b,c):
    if a == 0 or b == 0 or c == 0:
        return
    if a > 20 or b > 20 or c > 20:
        return
    if a < b < c:
        dp[a][b][c] = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
    else:
        dp[a][b][c] = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                dp[i][j][k] = 1

a = b = c = 0
for i in range(21):
    check(a,b,c)
    a += 1
    check(a,b,c)
    a -= 1
    b += 1
    check(a,b,c)
    b -= 1
    c += 1
    check(a,b,c)
    c -= 1
    a += 1
    b += 1
    check(a,b,c)
    b -= 1
    c += 1
    check(a,b,c)
    a -= 1
    b += 1
    check(a,b,c)
    a += 1

for i in range(21):
    for j in range(21):
        for k in range(21):
            check(i,j,k)

while True:
    x, y, z = map(int,input().split())

    if x == -1 and y == -1 and z == -1:
        break

    if x <= 0 or y <= 0 or z <= 0 :
        print(f'w({x}, {y}, {z}) = 1')
        continue
    
    if x > 20 or y > 20 or z > 20 :
        print(f'w({x}, {y}, {z}) = {dp[20][20][20]}')
        continue
    
    print(f'w({x}, {y}, {z}) = {dp[x][y][z]}')