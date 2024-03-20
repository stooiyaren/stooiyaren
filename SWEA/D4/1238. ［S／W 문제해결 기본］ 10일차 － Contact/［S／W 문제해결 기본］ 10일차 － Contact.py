from collections import deque

def bfs(start):
    q = deque()
    q.append([start,0])
    visited = [False] * 101
    visited[start] = True
    cnt = 0
    ans = [start]
    while q:
        s = q.popleft()
        
        if cnt < s[1]:
            cnt = s[1]
            ans = [s[0]]
        elif cnt == s[1]:
            ans.append(s[0])
        if s[0] in dic:
            for i in dic[s[0]]:
                if not visited[i]:
                    q.append([i,s[1]+1])
                    visited[i] = True
    ans.sort()
    return ans[-1]


for tc in range(1,11):
    people, start = map(int,input().split())
    dic = {}
    bridge = list(map(int,input().split()))
    for i in range(0,people,2):
        if bridge[i] in dic:
            dic[bridge[i]].append(bridge[i+1])
        else:
            dic[bridge[i]] = [bridge[i+1]]
    print(f'#{tc} {bfs(start)}')