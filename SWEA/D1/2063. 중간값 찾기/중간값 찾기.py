N = int(input())
my_list = list (map(int, input().split()))
my_list.sort()
a = N//2
print(my_list[a])