def tsn(n, ans):
    if n <10:
        if n in [3,6,9]:
            ans += '-'
            return ans
        else:
            if '-' in ans:
                return ans
            else:
                return '.'
    else:
        if n%10 in [3,6,9]:
            ans += '-'
        return tsn(n//10, ans)
        
N = int(input())
for i in range(1,N+1):
    ans = ''
    if '-' not in tsn(i,ans):
        print(i, end = ' ')
    else:
        print(tsn(i, ans), end = ' ')