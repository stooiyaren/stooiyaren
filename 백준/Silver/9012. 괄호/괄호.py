import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    ho = list(input().rstrip())
    stack = []
    ans = 1 # 정답 저장변수입니다. 0 이면 불가능, 1로 바뀌면 가능한 경우입니다.

    for i in ho: # 입력 값을 반복합니다.
        if i == '(': # 여는 괄호라면 스택에 추가합니다.
            stack.append(1)
        else: # 닫는 괄호가 들어가는 경우
            if not stack: # 스택이 비어있다면 괄호가 이루어지지 않습니다.
                ans = 0 # 불가능으로 변경합니다.
                break
            stack.pop() # 마지막 여는 괄호를 제거합니다.

    if stack: # 검사가 끝났는데 stack이 남아있다면 덜 닫힌 괄호이므로 불가능합니다.
        ans = 0
    
    if ans: # ans 의 여부로 출력합니다.
        print('YES')
    else:
        print('NO')