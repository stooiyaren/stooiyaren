N = int(input())
meeting = [0] * N
for n in range(N):
    start, end = map(int,input().split())
    meeting[n] = [start,end]

meeting.sort(key= lambda x: (x[1],x[0]))

time = 0
answer = 0
for i in meeting:
    if time <= i[0]:
        time = i[1]
        answer += 1
print(answer)