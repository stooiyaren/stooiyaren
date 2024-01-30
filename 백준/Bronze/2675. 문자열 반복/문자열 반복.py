T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    l = len(S)
    for j in range(l):
        print(S[j]*R,end='')
    print()