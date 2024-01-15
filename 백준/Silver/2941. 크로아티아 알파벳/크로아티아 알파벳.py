# 크로아티아 알파벳을 나타내는 문자열 리스트
cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

# 사용자로부터 문자열 입력 받기
word = str(input())
wl = len(word)

# 크로아티아 알파벳의 각 경우에 대해 개수 계산
for i in range(8):
    if i == 2:
        # 'dz='의 경우는 'dz='이 발생한 횟수에 2를 곱하여 계산
        count += 2 * word.count(cr[2])
    elif i == 7:
        # 'z='의 경우는 'dz='의 개수를 빼서 계산
        count += word.count(cr[7]) - word.count(cr[2])
    else:
        # 나머지 경우는 해당 크로아티아 알파벳의 개수를 계산
        count += word.count(cr[i])

# 결과 출력
print(wl - count)