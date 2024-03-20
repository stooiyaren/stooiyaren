# N을 두개로 나누는 방법
def devide(i,k):
    global mn

    if sum(bit) > N//2:
        return
    
    if i == k:
        if sum(bit) == N//2:
            left = [0] * (N//2)
            right = [0] * (N//2)
            l = 0
            r = 0
            # left = []
            # right = []
            for p in range(N):
                if bit[p]: # 비트가 1이라면 왼쪽에 0이라면 오른쪽에 넣습니다.
                    left[l] = arg[p]
                    l += 1
                    # left.append(arg[p])
                else:
                    right[r] = arg[p]
                    r += 1
                    # right.append(arg[p])
            # 만들어진 왼쪽 재료, 오른쪽 재료로 점수를 구합시다.
            balance = synergy(left,right) # 점수차를 balance 변수에 저장해서
            if balance < mn:
                mn = balance
                return
            else:
                return
        else:
            return

    bit[i] = 1
    devide(i+1,k)
    bit[i] = 0
    devide(i+1,k)

def synergy(A,B):
    global N
    # 리스트 A와 B가 들어온다면...
    Ascore = 0
    Bscore = 0
    for x in range(N//2): # 두 개를 고르기 위해 2중 for문 사용 시너지가 양방향이기 때문에 중복을 제거하지않게 N//2로 반복
        for y in range(N//2): # i == j인경우 0으로 주어지기 때문에 생각하지 않겠습니다! 다른 기호면 여기서 제거
            Ascore += ingredient[A[x]][A[y]]
            Bscore += ingredient[B[x]][B[y]]
    return abs(Ascore-Bscore) # 두 시너지 값의 차를 반환하겠습니다.

N = int(input())
ingredient = [list(map(int,input().split())) for _ in range(N)]
bit = [0]*N
arg = [i for i in range(N)]
mn = 20000*56
devide(0,N)
print(mn)