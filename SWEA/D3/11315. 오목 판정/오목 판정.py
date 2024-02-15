cro = [-1,1]
ss = [-1,1]

sip = [-1,1]
ja = [1,-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    gb = [list(input().rstrip()) for _ in range(N)]
    ans = 0
    
    for i in range(N):
        for j in range(N):
            cnt1 =0
            cnt2 =0
            if gb[i][j] == 'o':
                for k in range(2):
                    for l in range(1,3):
                        ni = i + cro[k]*l
                        nj = j + ss[k]*l
                        if 0<= ni < N and 0<= nj < N:
                            if gb[ni][nj] == 'o':
                                cnt1 += 1
                       
                        nx = i + sip[k]*l
                        ny = j + ja[k]*l
                        if 0<= nx < N and 0<= ny < N:
                            if gb[nx][ny] == 'o':
                                cnt2 += 1
            if cnt1 ==4:
                ans = 1
            if cnt2 ==4:
                ans = 1
        
    for i in gb:
        a = ''.join(i)
        if 'ooooo' in a:
            ans = 1
    gb = list(map(list,zip(*gb)))
    
    for i in gb:
        a = ''.join(i)
        if 'ooooo' in a:
            ans = 1
        
    if ans == 0:
        print(f'#{tc} NO')
    else:
        print(f'#{tc} YES')