def f(i, k, l):
    if i == k:
        if sum(bit) == l:
            for j in range(amount):
                if bit[j]:
                    print(number[j], end = ' ')
            print()
                
    else:
        bit[i] = 1
        f(i+1, k, l)
        bit[i] = 0
        f(i+1, k, l)
        
import sys
input = sys.stdin.readline

while True:
    number = list(map(int, input().split()))
    if number[0] == 0:
        break

    amount = number.pop(0)
    bit= [0] * amount
    lotto = [0] * 6
    f(0,amount,6)
    print()