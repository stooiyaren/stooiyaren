N = int(input())
n = 2
while N !=1 :
    if N%n ==0:
        print(n)
        N = N //n
        continue
    else:
        n +=1