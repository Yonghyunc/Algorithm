# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교
# 8/16


t = int(input())

for test_case in range(1, t + 1):

    # 각 문자열 입력
    str1, str2 = input(), input()

    # 각 문자열의 길이
    len1, len2 = len(str1), len(str2)

    for i in range(len2 - len1 + 1):
        if str2[i : i + len1] == str1:
            print(f'#{test_case} 1')
            break

    else:
        print(f'#{test_case} 0')
