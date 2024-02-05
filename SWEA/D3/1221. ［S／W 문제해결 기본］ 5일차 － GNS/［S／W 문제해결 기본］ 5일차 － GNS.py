number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())

for tc in range(1, T + 1):
    N, M = input().split()
    num = list(input().split()) 
    check = []
    soort = []

    for i in number:
        check.append(num.count(i))  

    for i in range(10):
        soort += [number[i]] * check[i] 

    print(N, *soort)