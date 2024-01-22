N, M = map(int, input().split())
L_S = 1000
L_A = 1000
for i in range(M):
    L6, L1 = map(int, input().split())
    if L6 < L_S:
        L_S = L6
    if L1 < L_A:
        L_A = L1

c = []
c.append(N*L_A)
c.append((N//6+1)*L_S)
c.append(N//6*L_S+N%6*L_A)
c.sort()
print(c[0])