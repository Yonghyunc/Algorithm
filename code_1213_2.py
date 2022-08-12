# 1213. [S/W 문제해결 기본] 3일차 - String
# 8/12


# 2. 반복문 활용

for t in range(1, 11):
    test_case = int(input())

    # 검색할 문자열
    search = input()

    # 문장
    string = input()

    # 검색할 문자열의 수
    sear_cnt = 0

    for i in range(len(string)):

        # 문자열의 개수만큼 슬라이싱
        if string[i : i + len(search)] == search:
            sear_cnt += 1

    print(f'#{test_case} {sear_cnt}')
