import sys
input = sys.stdin.readline

N = int(input())
vote=[]
for i in range(N):
    vote.append(int(input()))
    
if sum(vote) > N//2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')