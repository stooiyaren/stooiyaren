def check_parenthesis(S):
    ans = 'yes'
 # ----------------------------- 혹시 따옴표 안에 들어가있다면 제거하는 과정입니다. -----------
    stack = []
    for i in S:
        if i == "'" or i == '(' or i == ')' or i == '{' or i == '}' or i == '[' or i == ']':
            stack.append(i)
    for i in range(stack.count("'")//2):
        start= stack.index("'")
        end= stack.index("'", start + 1) + 1
        stack = stack[:start] + stack[end:]
 #----------------------------------------------------------------------------

    check = []
    
    for i in stack:
        if i == '(':
            check.append('(')
                
        elif i == '{':
            check.append('{')

        elif i == '[':
            check.append('[')            
    # --------------------------------- 괄호가 열리게 된다면 check에 추가합니다. ---------            
        elif i == ')':
            if '(' not in check:
                ans = 'no'
                break
            if check[-1] != '(':
                ans = 'no'
                break
            else:
                check.pop()
  
        elif i == '}':
            if '{' not in check:
                ans = 'no'
                break
            if check[-1] != '{':
                ans = 'no'
                break
            else:
                check.pop()

        elif i == ']':
            if '[' not in check:
                ans = 'no'
                break
            if check[-1] != '[':
                ans = 'no'
                break
            else:
                check.pop()                
    # ------------------------------------
    # 괄호가 닫히는 경우
    # 1. 열리지 않았다면 false입니다.
    # 2. 해당 괄호와 여는 괄호 사이에 다른 괄호가 열려있다면 false입니다.
    # 3. 이상이 없다면 check에서 여는 괄호를 제거해줍니다.
                           
    if check:
        ans = 'no'
    return ans

while True:
    a = input()
    if a == '.':
        break
    print(check_parenthesis(a))