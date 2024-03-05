import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

string = input().rstrip()
check = set()
s = len(string)
for i in range(s):
    for j in range(i+1,s+1):
        check.add(string[i:j])
print(len(check))