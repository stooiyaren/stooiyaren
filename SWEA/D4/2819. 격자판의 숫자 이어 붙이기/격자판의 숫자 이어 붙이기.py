from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    global ans

    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        if start[3] == 7:
            ans.add(tuple(start[2]))
            continue
        else:
            for i in range(4):
                di = start[0] + dx[i]
                dj = start[1] + dy[i]

                if 0 <= di < 4 and 0 <= dj < 4:
                    # start[2][start[3]] = square[di][dj]
                    q.append([di,dj,start[2]+[square[di][dj]],start[3]+1])
T = int(input())
for tc in range(1,T+1):
    square = [list(map(int,input().split())) for _ in range(4)]
    ans = set()
    # cnt = [0] * 7
    for i in range(4):
        for j in range(4):
            # cnt[0] = square[i][j]
            bfs([i,j, [square[i][j]],1])
    # print(ans)
    print(f'#{tc} {len(ans)}')