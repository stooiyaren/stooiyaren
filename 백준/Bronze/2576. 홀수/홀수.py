import sys
input = sys.stdin.readline

num = []
for i in range(7):
    n = int(input())
    if n %2 == 1:
        if not num:
            odd_num = n
        if n < odd_num:
            odd_num = n
        num.append(n)
if not num:
    print(-1)
else:
    print(sum(num))
    print(odd_num)