def thriary(i):
    global N, check, ans
    # i까지 검사했을때 같은 패턴이 두번 반복되는게 있다면 prunning
    if check: # 정답이 나와있으면 빨리 끝내죠 남은친구 모두 prunning
        return


    for j in range(1,(i//2+1)): # 한개 한개 두개 두개 세개 세개 비교해야됨
        # j 갯수씩 비교
        num1 = ans[i-j:i]
        num2 = ans[i-2*j:i-j]
        if num1 == num2:
            return

    if i == N:
        print(''.join(map(str,ans)))        
        check = 1 # 가장먼저 구해지는 놈이 정답입니다 1부터 작은순서대로 구했으니        
        return

    ans[i] = 1
    thriary(i+1)
    ans[i] = 2
    thriary(i+1)
    ans[i] = 3
    thriary(i+1)
    

N = int(input())
ans = [0]*N
check = 0
thriary(0)