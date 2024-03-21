from collections import deque

def bfs(start):
    global ans
    q = deque()
    q.append([S,0])

    while q:
        start, cnt = q.popleft()

        if start + U == G or start - D == G:
            ans = cnt+1
            return 1

        if start+U < F+1 and not floor[start+U]:
            q.append([start + U, cnt+1])
            floor[start+U] = True
        if 0 < start-D and not floor[start-D]:
            q.append([start - D, cnt+1])
            floor[start-D] = True
    return 0

F,S,G,U,D = map(int,input().split())

floor = [False] * (F+1)
ans = 0
if S == G:
    print(0)
else:
    floor[0] = True
    floor[S] = True
    if bfs(S):
        print(ans)
    else:
        print('use the stairs')