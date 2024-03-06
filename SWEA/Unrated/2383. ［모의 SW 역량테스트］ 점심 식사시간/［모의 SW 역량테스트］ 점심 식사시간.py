def xit(point): # 게단과 사람과의 거리를 계산해서 반환합니다.
    dxit = []
    for i in stair:
        dxit.append(abs(point[0] - i[0])+abs(point[1] - i[1]))
    return dxit

def check(i,k):
    if i == k:
        cnt = []
        for p in range(k):
            cnt.append(bit[p])
        eexxiitt.append(cnt)
        return
    else:
        bit[i] = 0
        check(i+1,k)
        bit[i] = 1
        check(i+1,k)

# [[거리,계단 시간]]
def discend0():
    cnt = 0
    stair0 = []   
    while True:
        if not stair0 and not st0: # 사람도 없고 계단도 없다면 종료합시다.
            return cnt       
        if stair0: # 먼저 계단을 내려갑시다. 계단을 내려가고 있는 사람이 있다면
            for i in range(len(stair0)):
                stair0[i] -= 1
            
            while 0 in stair0:
                stair0.remove(0)

        if st0:
            while st0 and len(stair0) < 3: # 사람이 있고 계단이 빈다면 돌립시다.
                if st0[0] < cnt:
                    st0.pop(0) # 사람은 계단에 넣고
                    stair0.append(stair[0][2]) # 계단엔 내려가는 시간을 넣죠
                else:
                    break
        if not stair0 and not st0: # 사람도 없고 계단도 없다면 종료합시다.
            return cnt

        cnt += 1 # 1분이 지납니다.
        
def discend1():
    cnt = 0
    stair1 = []   
    while True:
        if not stair1 and not st1: # 사람도 없고 계단도 없다면 종료합시다.
            return cnt
        
        if stair1: # 계단을 내려갑시다.
            for i in range(len(stair1)):
                stair1[i] -= 1
            
            while 0 in stair1:
                stair1.remove(0)

        if st1:
            while st1 and len(stair1) < 3: # 계단이 남아있고 사람이 도착해있다면
                if st1[0] < cnt: 
                    st1.pop(0) # 사람은 계단에 넣고
                    stair1.append(stair[1][2]) # 계단엔 내려가는 시간을 넣죠
                else:
                    break
        if not stair1 and not st1: # 사람도 없고 계단도 없다면 종료합시다.
            return cnt

        cnt += 1

# ----------------------- function line ------------------------
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    
    floor = [list(map(int,input().split())) for _ in range(N)] # 이번 층의 정보를 받아옵니다.
    stair = []
    for i in range(N):
        for j in range(N):
            if floor[i][j] != 0 and floor[i][j] != 1: # 0과 1이 아니라면 계단입니다.
                stair.append([i,j,floor[i][j]]) # 계단의 좌표와 계단을 내려가는 시간을 리스트로 저장합니다.
    person = []
    for i in range(N):
        for j in range(N):
            if floor[i][j] == 1: # 1은 사람입니다.
                point = [i,j] # 좌표를 받아서
                person.append(xit(point)) # 계단과의 거리를 계산해 리스트에 넣습니다.

    n = len(person) # 사람 수를 토대로 계단을 쓸 수 있는 리스트를 생성합니다.
    bit = [0] * n
    eexxiitt = [] # 각 사람이 사용하는 계단을 저장합니다.
    check(0,n)

    ans = 3000
    for i in eexxiitt:
        mn1 = 0
        mn2 = 0
        st0 = []
        st1 = []
        for j in range(len(i)):
            if i[j] == 0: # 0이면 0번 계단을 쓰시고
                st0.append(person[j][0])
            else: # 1이면 1번 계단을 쓰세요
                st1.append(person[j][1])
        st0.sort() # 도착하는 순서대로 정렬
        st1.sort()

        mn1 += discend0() # 0번 계단으로 내려간 시간
        
        mn2 += discend1() # 1번 계단으로 내려간 시간
        
        if ans > max(mn1,mn2):
            ans = max(mn1,mn2)   
    
    print(f'#{tc}', ans)