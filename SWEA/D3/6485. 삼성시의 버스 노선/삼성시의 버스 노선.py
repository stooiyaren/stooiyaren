T = int(input())
for i in range(1,T+1):
    N = int(input())
    count = [0] * 5001
    answer = []
    for p in range(N):
        a, b = map(int,input().split())
        for q in range(a,b+1):
            count[q] +=1

    P = int(input())
    for k in range(P):
        j = int(input())
        answer.append(count[j])
    print(f'#{i}', *answer)