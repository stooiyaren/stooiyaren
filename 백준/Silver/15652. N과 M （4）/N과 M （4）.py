def c(i):
    global check
    if i == M:  # 선택한 숫자의 개수가 M이면 결과를 출력
        print(*ans)
        return

    # i가 0이거나 현재 숫자가 이전 숫자 이상일 때만 다음 단계로 진행
    start = ans[i-1] if i > 0 else 1
    for j in range(start, N+1):
        ans[i] = j
        c(i+1)

N, M = map(int, input().split())
ans = [0] * M
check = []
c(0)