N = int(input())
a = 1
b = N
while N > 0:
     print(f"{' '*(b-a)}{'*'*a}")
     a += 1
     N -= 1