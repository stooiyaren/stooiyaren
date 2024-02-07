def check_parenthesis(S):
    stack = []
    cnt = 0
    befo = ''
    for i in S:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if befo == '(':
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
        befo = i
    return cnt

T = int(input())
for tc in range(1,T+1):
    steel_stick = input()
    print(f'#{tc}', check_parenthesis(steel_stick))