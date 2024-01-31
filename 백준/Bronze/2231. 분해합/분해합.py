import sys
input = sys.stdin.readline

N = int(input())

def divide(N):
	for i in range(1, N):
		hap = i+ sum(map(int, str(i)))
		
		if hap == N:
			return i
	return 0

print(divide(N))