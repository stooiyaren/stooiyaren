import sys
input = sys.stdin.readline

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

print(round(sum(num)/N)) # 산술평균

num.sort()
print(num[N//2]) # 중앙값

cntx = 0
cnt = []
cnum = set(num)
for i in cnum:
    if cntx < num.count(i):
        cntx = num.count(i)
        cnt = [i]
    elif cntx == num.count(i):
        cnt.append(i)
cnt.sort()
if len(cnt) == 1:
    print(cnt[0])
else:
    print(cnt[1])

print(max(num)-min(num)) # 범위