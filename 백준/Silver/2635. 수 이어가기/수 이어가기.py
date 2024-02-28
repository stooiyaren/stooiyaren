def chain(n):
    global mx
    global ans

    if n < 0:
        if mx < len(number):
            mx = len(number)
            ans = number.copy()
        return
    number.append(n)
    chain(number[-2]-number[-1])
    number.pop()

number = []
mx = 0
ans = 0
n = int(input())
number.append(n)
if n == 1:
    print(4)
    print(f'1 1 0 1')
else:
    for i in range(1,n):
        chain(i)
    
    print(mx)
    print(' '.join(map(str, ans)))