import sys
input = sys.stdin.readline

for i in range(3):
   uch = list(map(int, input().split()))
   if sum(uch) == 0:
      print('D')
   elif sum(uch) == 1:
      print('C')
   elif sum(uch) == 2:
      print('B')
   elif sum(uch) == 3:
      print('A')
   elif sum(uch) == 4:
      print('E')