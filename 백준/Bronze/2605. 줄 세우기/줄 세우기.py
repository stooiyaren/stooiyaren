from collections import deque

N =int(input())
student = deque()
card = list(map(int,input().split()))
card = [0] + card
for i in range(1,N+1):
    if card[i] == 0:
        student.append(i)
    else:
        student.rotate(card[i])
        student.append(i)
        student.rotate(-card[i])
print(*student)