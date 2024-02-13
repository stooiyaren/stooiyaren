import math

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    movement = [0] * 201
    for i in range(N):
        a, b = map(int,input().split())
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        start = min(a,b)
        end = max(a,b)

        for j in range(start,end+1):
            movement[j] += 1
        
    print(f'#{tc} {max(movement)}')