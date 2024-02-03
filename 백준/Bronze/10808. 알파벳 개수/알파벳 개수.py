import sys
input = sys.stdin.readline

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i' ,'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
check = dict.fromkeys(alphabet,0)

word = list(map(str,input()))

for i in word:
    if i in alphabet:
        check[i] += 1

print(*check.values())