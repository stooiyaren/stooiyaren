string = input()
stack = []
ans = 1
for i in string:
    if i == '(' or i == '[':
        stack.append(i)
    else:
        if i == ')':
            store = 0
            if not stack: # 혼자서 닫는 괄호면 버리면 됩니다.
                ans = 0
                break
            if isinstance(stack[-1],int):
                store = stack.pop()
            if not stack:
                ans = 0
                break
            if stack[-1] == '(': # ) 전에 ( 이면
                stack.pop()
                if store:
                    stack.append(2*store)
                else:
                    stack.append(2)
            else:
                ans = 0
                break    
        elif i == ']':
            store = 0
            if not stack:
                ans = 0
                break
            if isinstance(stack[-1],int):
                store = stack.pop()
            if not stack:
                ans = 0
                break
            if stack[-1] == '[':
                stack.pop()
                if store:
                    stack.append(3*store)
                else:
                    stack.append(3)
            else:
                ans = 0
                break
        if len(stack) > 1:
            if isinstance(stack[-2],int) and isinstance(stack[-1],int):
                a = stack.pop()
                stack[-1] += a        

if not ans:
    print(ans)
else:
    if len(stack) == 1 and isinstance(stack[0],int):
        print(stack[0])
    else:
        print(0)