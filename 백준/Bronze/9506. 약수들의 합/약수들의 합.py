n = int(input())
while n != -1:
    d = []
    for i in range(1,n):
        if n%i==0:
            d.append(i)
    if sum(d) == n:
        print(n,'=',' + '.join(map(str,d)))
    else:
        print(f"{n} is NOT perfect.")
    n = int(input())