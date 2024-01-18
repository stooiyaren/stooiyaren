N, B = map(int, input().split())
num = []

while N > 0:
    T = N % B
    if T > 9:
        T = chr(T + 55)
    num.append(str(T))
    N = N // B

print(''.join(num[::-1]))