for i in range(1, 11):
    dump = int(input())
    m = list(map(int, input().split()))

    for _ in range(dump):
        max_index = m.index(max(m))
        min_index = m.index(min(m))

        m[max_index] -= 1
        m[min_index] += 1

        if max(m) == min(m):
            break
        if m.count(max(m)) == 99:
            break

    result = max(m) - min(m)
    print(f'#{i} {result}')