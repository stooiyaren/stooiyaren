import sys
input = sys.stdin.readline

x = '('
y = ')'
T = int(input())
for i in range(T):
    n = input()
    cnt = 0
    x_cnt = 0
    y_cnt = 0
    for j in n:
        if j == 0 and j == y:
            cnt -= 1
        
        if j == x:
            x_cnt += 1
        elif j == y:
            y_cnt += 1
        
        if x_cnt < y_cnt:
            cnt -= 1
    
    if x_cnt != y_cnt:
        cnt -= 1

    if cnt ==0:
        print('YES')
    elif cnt < 0:
        print('NO')