def postfix(text):
    stack = [] # push : append() / pop : pop()
    result = ''
    for i in text:
        # (
        if i == '(':
            stack.append(i)
        # */
        elif i == '*' or i== '/':
            # 스택에 들어있는 값이 * / 연산자라면 빼준다
            if stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)            
        # +-
        elif i =='+' or i == '-':
            # 여는 괄호가 나오거나 스택이 아예 빌 경우까지 pop을 계속 진행해준다
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        # )
        elif i == ')':
            # 여는 괄호가 나올 때까지 pop 해줘라
            while stack[-1] != '(':                
                result += stack.pop()
            stack.pop()
        # 숫자
        elif i.isdigit():
            result += i
        # 스택을 모두 pop
        
    while stack:
        result += stack.pop()
    return result

def middlewe(text):
    stack = []
    for i in text:
        if i.isdigit():
            stack.append(i)
        
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if i == '*':
                stack.append(a*b)
            elif i == '/':
                stack.append(a//b)
            if i == '+':
                stack.append(a+b)
            if i == '-':
                stack.append(a-b)
    return stack[0]

for tc in range(1,11):
    n = int(input())
    text = input()
    print(f'#{tc}', middlewe(postfix(text)))