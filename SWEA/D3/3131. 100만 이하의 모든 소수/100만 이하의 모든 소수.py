number = list(range(1000001))
prime = []
for i in range(2,1000001):
    if number[i] == 0:
        continue
    for j in range(i*i,1000001,i):
        number[j] = 0
for i in number:
    if i !=0:
        prime.append(i)
prime.remove(1)
print(*prime)