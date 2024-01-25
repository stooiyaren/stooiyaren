import sys
input = sys.stdin.readline

n = int(input())
chang = 100
sang = 100
for i in range(n):
    c_dice, s_dice = map(int, input().split())
    if c_dice == s_dice:
        continue
    elif c_dice > s_dice:
        sang -= c_dice
    elif c_dice < s_dice:
        chang -= s_dice
print(chang)
print(sang)