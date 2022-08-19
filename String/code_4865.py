# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수
# 8/16

t = int(input())

for test_case in range(1, t + 1):
    str1, str2 = input(), input()

    cnt = 0

    for i in range(len(str1)):
        if cnt < str2.count(str1[i]):
            cnt = str2.count(str1[i])

    print(f'#{test_case} {cnt}')
