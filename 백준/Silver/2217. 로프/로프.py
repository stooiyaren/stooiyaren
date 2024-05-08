N = int(input())
rope = [0] * N
for n in range(N):
    rope[n] = int(input())
rope.sort(reverse=True)
mx = rope[0]
for i in range(1,N):
    if rope[i]*(i+1) > mx:
        mx = rope[i]*(i+1)
print(mx)