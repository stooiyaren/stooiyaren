N = int(input())
cnt =1
for i in range(N):
    print(f"{'*'*cnt}{' '*((2*N)-2*cnt)}{'*'*cnt}")
    cnt +=1
cnt -= 1
for i in range(N-1,0,-1):
    cnt -=1
    print(f"{'*'*cnt}{' '*((2*N)-2*cnt)}{'*'*cnt}")