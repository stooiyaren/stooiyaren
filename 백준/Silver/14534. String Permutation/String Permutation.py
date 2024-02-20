from itertools import permutations

T = int(input())
for tc in range(1,T+1):
    n = list(input())

    ans = list(permutations(n,len(n)))
    print(f'Case # {tc}:')
    for i in ans:
        print(''.join(i))