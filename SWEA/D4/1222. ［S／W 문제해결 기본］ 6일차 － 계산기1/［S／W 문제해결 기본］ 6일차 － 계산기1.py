for tc in range(1,11):
    N = int(input())
    string = map(int,input().split('+'))
    print(f'#{tc}', sum(string))