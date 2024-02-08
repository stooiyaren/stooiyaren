N = int(input())

scores = [int(input()) for _ in range(N)]


if N == 1:
    print(scores[0])

elif N == 2:
    print(scores[0] + scores[1])

else:
    dp = [0] * (N+1)

    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])


    for x in range(3, N):
        dp[x] = max(dp[x-2] + scores[x], dp[x-3] + scores[x] + scores[x-1])

    print(dp[N-1])