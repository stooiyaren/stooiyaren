num = [1,2,3,4,5,6,7,8,9] # 스도쿠 확인용 1-9 리스트 입니다.
T = int(input())
for tc in range(1,T+1):
    doku =[list(map(int,input().split())) for _ in range(9)]
    s = 1
 # ------------------------------ input ----------------------

    for i in range(9): # 가로줄은 이미 list로 생성되기 때문에 바로 확인합니다.
        if num != sorted(doku[i]): # 확인용 리스트 num과 가로줄을 비교합니다.
            s = 0
 
    for i in range(0,9,3): # 3,3을 돌면서 3*3 스퀘어를 확인합니다.
        for j in range(0,9,3):
            d =[] # d에 3*3 스퀘어의 수를 저장합니다.
            for p in range(3):
                for q in range(3):
                    d.append(doku[i+p][j+q])
            d.sort() # d를 오름차순으로 정렬해서 num과 비교합니다.
            if num != d:
                s = 0
 
    doku = [list(t_row) for t_row in zip(*doku)] # 전치행렬로 만듭니다.
    for i in doku: # 새로만들어진 전치행렬의 가로줄은 기존의 세로줄과 같습니다.
        i.sort() #(이렇게 정렬해버리면 doku가 바뀌기 때문에 마지막에서만 야매로 사용했습니다.)
        if num != i:
            s = 0
    print(f'#{tc} {s}') # 한번이라도 어긋난다면 0을 모두 가능하다면 1을 출력합니다.