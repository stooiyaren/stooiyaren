import sys
import math
input = sys.stdin.readline

N = int(input())

tree = int(input())
check1 = tree
first = tree

tree = int(input())
check2 = tree

tree1 = int(input())
dis = math.gcd(tree1 - check2,check2 - check1)

if N >= 4:
    for i in range(N-4):
        tree = int(input())
        dis = math.gcd(tree - tree1,dis)
        tree1 = tree

    tree = int(input())
    last = tree
    dis = math.gcd(dis, tree - tree1)
    print((last - first)//dis - N +1)
    
else:
    last = tree1
    print((last - first)//dis - N +1)