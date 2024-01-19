N = int(input())
count = 0
n = 1
if N == 1:
    print(1)
else:
    while ((N-1) > (3*n*(n+1))):        
        count += 1
        n += 1
    print(count+2)