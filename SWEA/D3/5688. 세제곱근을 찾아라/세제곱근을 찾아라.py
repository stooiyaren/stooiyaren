def binary(key):
    start = 1
    end = key
    while start <= end:
        middle = (start + end)//2
        if middle**3 == key:
            return middle
        elif middle**3 > key:
            end = middle -1
        else:
            start = middle + 1
    return -1
        
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    print(f'#{tc}', binary(n))