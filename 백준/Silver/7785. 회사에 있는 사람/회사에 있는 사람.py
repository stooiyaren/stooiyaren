import sys
input = sys.stdin.readline

N = int(input())
member = []
for i in range(N):
    name, inform = input().split()
    if inform == 'enter':
        member.append(name)
    else:
        member.remove(name)

member.sort()
for i in range(len(member)-1,-1,-1):
    print(member[i])