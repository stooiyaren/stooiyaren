dx = [0,0,1,0,-1] # 상우하좌
dy = [0,-1,0,1,0]

def construct(bc): # bc는 리스트 형태 [충전기 x좌표, 충전기 y좌표, 범위, 충전량, 충전기 번호]
    for i in range(10):
        for j in range(10):
            if 0<= bc[0]-1 < 10 and 0<= bc[1]-1 < 10:
                if bc[2] >= abs(bc[0]-1-i)+abs(bc[1]-1-j): # 충전 범위 내에 있는 칸이라면
                    jido[i][j].append(bc[4]) # jido에 충전기 번호를 추가

T = int(input())
for tc in range(1,T+1):
    M, A = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    jido = [[[] for _ in range(10)] for _ in range(10)]
    a_cor = [0,0] # cordinate가 좌표랍니다. a좌표
    b_cor = [9,9]
    BC = []
    ans = 0

    for i in range(A):
        device = list(map(int,input().split())) #[x,y,범위,충전량]
        BC.append(device)

    # BC를 리스트의 네번째 값대로 내림차 sort 하면서 인덱스를 추가해줄까?
    BC.sort(key = lambda x:x[3],reverse=True)
    for i in range(A): # 충전기의 인덱스별로 번호를 부여
        BC[i].append(i+1)
    BC = [[0]] + BC

    for i in range(1,A+1): # 충전기를 지도에 설치합니다.
        construct(BC[i])

    # for i in jido:
    #     print(*i)
    # print()


    for i in range(M+1): # 이동시간만큼 이동
        # a와 b의 좌표를 토대로 해당 칸을 조사
        # 둘다 충전기가 있다면
        if jido[a_cor[0]][a_cor[1]] and jido[b_cor[0]][b_cor[1]]:
            if jido[a_cor[0]][a_cor[1]][0] != jido[b_cor[0]][b_cor[1]][0]: # 강한 충전기가 다르다면 그냥 더해요
                ans += BC[jido[a_cor[0]][a_cor[1]][0]][3] + BC[jido[b_cor[0]][b_cor[1]][0]][3]
            else: # 강한 충전기가 같을 때
                if len(jido[a_cor[0]][a_cor[1]]) == len(jido[b_cor[0]][b_cor[1]]) and len(jido[a_cor[0]][a_cor[1]]) == 1:
                    ans += BC[jido[a_cor[0]][a_cor[1]][0]][3] # 서로 한개씩 뿐이라면 반띵해서 더하니깐 한번 더해줍니다.
                elif len(jido[a_cor[0]][a_cor[1]]) == 1:
                    ans += BC[jido[a_cor[0]][a_cor[1]][0]][3] + BC[jido[b_cor[0]][b_cor[1]][1]][3]
                elif len(jido[b_cor[0]][b_cor[1]]) == 1:
                    ans += BC[jido[b_cor[0]][b_cor[1]][0]][3] + BC[jido[a_cor[0]][a_cor[1]][1]][3]
                else:
                    if jido[a_cor[0]][a_cor[1]][1] < jido[b_cor[0]][b_cor[1]][1]:
                        ans += BC[jido[a_cor[0]][a_cor[1]][1]][3] + BC[jido[b_cor[0]][b_cor[1]][0]][3]
                    else:
                        ans += BC[jido[b_cor[0]][b_cor[1]][1]][3] + BC[jido[a_cor[0]][a_cor[1]][0]][3]

        else:
            if jido[a_cor[0]][a_cor[1]]: # a만 충전위치에 있다면
                ans += BC[jido[a_cor[0]][a_cor[1]][0]][3] # 가장 충전량 높은 BC의 충전량을 더함
            elif jido[b_cor[0]][b_cor[1]]:  # b만 충전위치에 있다면
                ans += BC[jido[b_cor[0]][b_cor[1]][0]][3]  # 가장 충전량 높은 BC의 충전량을 더함
            else: # 둘 다 충전 위치에 없다면 pass
                pass
        # 이동을 합시다.
        if i == M:
            break
        a_cor = [a_cor[0]+dx[a[i]], a_cor[1]+dy[a[i]]]
        b_cor = [b_cor[0]+dx[b[i]], b_cor[1]+dy[b[i]]]

    print(f'#{tc}', ans)