from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))

best = 0
for res in combinations(card, 3):
    if best < sum(res) <= M:
        best = sum(res)
print(best)