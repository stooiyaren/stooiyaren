T = int(input())
for tc in range(1,T+1):
        N = int(input())
        tree = list(map(int,input().split()))

        water = [0] * N

        odd = even = 0

        for i in range(N):
                water[i] = max(tree) - tree[i]

                if water[i]%2:
                        odd += 1

                even += water[i]//2

        if odd > even:
                print(f'#{tc} {2*odd - 1}')
        elif odd == even:
                print(f'#{tc} {2*odd}')
        else:
                check = (sum(water) - 3*odd)//2
                if check%3:
                        print(f'#{tc} {2*odd + check//3 * 4 + check%3+1}')
                else:
                        print(f'#{tc} {2*odd + check//3 * 4}')