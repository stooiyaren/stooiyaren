N, B = input().split()
N = list(N)
B = int(B)
count = 0

for i in range(len(N)-1, -1, -1):  
    if N[i] not in '0123456789': 
        N[i] = int(ord(N[i]) - 55)
    else:
        N[i] = int(N[i])
    count += N[i] * (B ** (len(N)-1-i))

print(count)