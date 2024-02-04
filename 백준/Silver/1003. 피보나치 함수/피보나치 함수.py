def fibo_memo(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fibo_memo(n-1, memo) + fibo_memo(n-2, memo)
        memo[n] = result
        return result

import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    memo = {}
    if n != 0:
        print(f"{fibo_memo(n-1, memo)} {fibo_memo(n, memo)}")
    elif n == 0:
        print(f"1 0")