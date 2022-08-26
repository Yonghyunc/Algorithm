# 1859. 백만 장자 프로젝트
# string 실습 extra


import sys

sys.stdin = open('../input_1.txt')


t = int(input())

for test_case in range(1, t + 1):
    n = int(input())

    nums = list(map(int, input().split()))

    income = []

    for i in range(n - 1, -1, -1):
        # 구매 시 사용한 요금
        buy = 0
        for j in range(i):
            buy += nums[j]
        # 판매이익이 요금보다 많다면 income 리스트에 추가
        for k in range(n - i):
            if nums[k] * i > buy:
                income.append(nums[k] * i - buy)

    max_income = 0

    # 이익이 없을 때
    if len(income) == 0:
        max_income = 0

    # 최대 이익
    for i in range(len(income)):
        if max_income < income[i]:
            max_income = income[i]

    print(f'#{test_case} {max_income}')
