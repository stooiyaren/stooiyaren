import sys
input = sys.stdin.readline


a, b, c, d, e, f = map(int,input().split())
lst = []
for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i + b*j ==c:
            lst.append([i,j])
answer = []
for i in range(len(lst)):
    if d*lst[i][0] + e*lst[i][1] == f:
        answer.append([lst[i][0],lst[i][1]])
print(answer[0][0], answer[0][1])