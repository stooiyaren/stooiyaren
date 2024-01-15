T = int(input())
for i in range(1,T+1):
    number1, number2 = map(int, input().split())
    if number1 < number2:
        print(f"#{i} <")
    elif number1 == number2:
        print(f"#{i} =")
    elif number1 > number2:
        print(f"#{i} >")
