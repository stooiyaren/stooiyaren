def DFS(start, end):
    visited = [start]
    stack = [start]
    while True:
        if route1[start] and route1[start] not in visited:
            start = route1[start]
            visited.append(start)
            stack.append(start)
        elif route1[start] and route1[start] in visited:
            if route2[start]:
                start = route2[start]
                stack.append(start)
                visited.append(start)
            else:
                if not stack:
                    return 0
                else:
                    start = stack.pop()
        else:
            if not stack:
                return 0
            else:
                start = stack.pop()
                    
        if start == end:
            return 1
                
for tc in range(1,11):
    test, road = map(int, input().split())
    connect = list(map(int, input().split()))
    route1 = ['']*100
    route2 = ['']*100
    for i in range(road):
        if route1[connect[2*i]]:
            route2[connect[2*i]] = connect[2*i+1]
        else:
            route1[connect[2*i]] = connect[2*i+1]
    print(f'#{tc}', DFS(0,99))