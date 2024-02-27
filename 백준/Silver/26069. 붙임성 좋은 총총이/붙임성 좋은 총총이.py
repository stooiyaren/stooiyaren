n = int(input())
dance = ['ChongChong']
for i in range(n):
    person, human = input().split()
    if person in dance and human not in dance:
        dance.append(human)
    if person not in dance and human in dance:
        dance.append(person)
print(len(dance))