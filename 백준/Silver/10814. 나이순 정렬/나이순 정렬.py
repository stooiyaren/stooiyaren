import sys
input = sys.stdin.readline

N = int(input())
member ={}

for i in range(N):
    age, name = input().split()
    age = int(age)

    if age not in member:
        member[age] = []
    member[age].append(name)

sort_age = sorted(member.keys())

for age in sort_age:
    for name in member[age]:
        print(f'{age} {name}')