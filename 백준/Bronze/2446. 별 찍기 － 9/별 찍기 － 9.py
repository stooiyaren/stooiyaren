N = int(input())
cnt = 0
for i in range(N):
    print(f"{' '*cnt}{'*'*(2*(N-cnt)-1)}")
    cnt +=1
cnt -=2
for i in range(N,1,-1):
    print(f"{' '*cnt}{'*'*(2*(N-cnt)-1)}")
    cnt -=1