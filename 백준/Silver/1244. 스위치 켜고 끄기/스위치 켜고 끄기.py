def male(number):
    for i in range(number,swich+1,number):
        switch[i] ^= 1

def female(number):
    i = 0
    while True:
        if swich < number + i or number - i <= 0:
            for j in range(i):
                switch[number + j] ^= 1
                switch[number - j] ^= 1
            switch[number] ^= 1
            return

        if switch[number + i] == switch[number - i]:
            i += 1
            continue
        else:
            if i == 0:
                switch[number] ^= 1
            else:
                for j in range(i):
                    switch[number + j] ^= 1
                    switch[number - j] ^= 1
                switch[number] ^= 1
            return


swich = int(input())
switch = list(map(int,input().split()))
switch = [0] + switch
student = int(input())
for inform in range(student):
    gender, number = map(int,input().split())

    if gender == 1:
        male(number)
    elif gender == 2:
        female(number)
ans = switch[1:]
while len(ans) >= 20:
    print(' '.join(map(str,ans[:20])))
    ans = ans[20:]
print(' '.join(map(str,ans)))