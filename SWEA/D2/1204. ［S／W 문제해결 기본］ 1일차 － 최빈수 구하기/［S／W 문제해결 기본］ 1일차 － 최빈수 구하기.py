T = int(input())

for i in range(T):
    seq = input()
    grade = list(map(int, input().split()))

    max_grade = 0
    max_count = 0
    amount = [0]*101
    
    for j in range(1000):
        amount[grade[j]] += 1

    for j in range(1, 101):
        count = amount[j]
        if count >= max_count:
            max_count = count
            max_grade = j

    print(f'#{seq} {max_grade}')