T = int(input())
for tc in range(1,T+1):
    s = str(input().strip())

    if s == s[::-1]: # 입력받은 문자열과 입력받은 문자열을 역순으로 재배열한 문이 같다면 회문입니다.
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')