import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
member = set()
for i in range(N):
    typing = input().rstrip()
    if typing == 'ENTER':
        cnt += len(member)
        member = set()
    else:
        member.add(typing)
cnt += len(member)
print(cnt)