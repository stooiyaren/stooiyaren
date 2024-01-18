def square(n,memo):
    if n ==1:
        return 3
    elif n in memo:
        return memo[n]
    else:
        result = 2 * square(n-1,memo) -1
        memo[n] = result
        return result

N = int(input())
memo ={}
print(square(N,memo)**2)