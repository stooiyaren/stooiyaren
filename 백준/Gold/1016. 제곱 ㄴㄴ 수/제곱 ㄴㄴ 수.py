mn, mx = map(int,input().split())

check = [1]*(mx-mn+1)
cnt = mx-mn+1
m = int(mx**0.5)
#prime = [1] * (m+1)
for i in range(2,m+1):
#    if prime[i]:
#        if i < m**0.5:
#            for j in range(i*i,m+1,i):
#                prime[j] = 0
        for j in range(((mn-1)//(i*i)+1)*(i*i),mx+1,i*i):
                check[j-mn] = 0
print(sum(check))