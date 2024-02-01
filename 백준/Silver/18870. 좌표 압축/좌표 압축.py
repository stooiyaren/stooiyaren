def binary(arr,key):
    start = 0
    end = len(arr)
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            end = middle
        elif arr[middle] < key:
            start = middle

import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
fix = sorted(set(X))

for i in X:
    print(binary(fix,i), end=' ')