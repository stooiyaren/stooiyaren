import sys
input = sys.stdin.readline

N = int(input())
number = list(range(98690))
ans = ''
for i in range(2,98690):
    if number[i] == 0:
        continue
    if str(i) == str(i)[::-1] and N <= i:
        ans = i
        break
    for j in range(i*i,98690,i):
        number[j] = 0
    if ans != '':
        break
if ans == '':
    ans = 1003001
print(ans)