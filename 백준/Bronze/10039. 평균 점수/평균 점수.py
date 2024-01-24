import sys
intput = sys.stdin.readline

one = int(input())
seh = int(input())
sang = int(input())
sung = int(input())
gang = int(input())

score = [one,seh,sang,sung,gang]
for i in range(len(score)):
    if score[i] < 40:
        score[i] = 40
print(sum(score)//5)