# 5356. 의석이의 세로로 말해요
# 8/ 16

t = int(input())

for test_case in range(1, t + 1):
    all = [0] * 5

    for i in range(5):
        all[i] = input()

    # 최장 문자열 길이 구하기
    maxlen = 0

    for i in range(5):
        if maxlen < len(all[i]):
            maxlen = len(all[i])

    # 최장 문자열 길이만큼 빈칸 삽입
    for i in range(5):
        all[i] += " " * (maxlen - len(all[i]))

    # 문자열 한 줄로 만들기
    one = ""
    for i in range(maxlen):
        for j in range(5):
            one += all[j][i]

    # 공백 제거 한 문자열 출력
    print(f'#{test_case} {one.replace(" ", "")}')
