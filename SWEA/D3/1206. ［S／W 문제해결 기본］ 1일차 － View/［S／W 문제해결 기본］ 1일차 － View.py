for i in range(1,11):
    N = int(input())
    building = list(map(int,input().split()))
    cnt = 0
    for j in range(2,N-2):
        if building[j-2] < building[j] and building[j-1] < building[j] and building[j+2] < building[j] and building[j+1] < building[j]:
            cnt += building[j] - max(building[j-2],building[j-1],building[j+1],building[j+2])
    print(f'#{i} {cnt}')