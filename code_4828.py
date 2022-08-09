# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max
# 8/9


# 테스트 케이스 수
t = int(input())

for test_case in range(1, t + 1):

    # 양수 개수
    n = int(input())

    # n개의 양수
    nums = list(map(int, input().split()))

    max_n = nums[0]
    min_n = nums[0]

    for i in range(n):

        # 최대값
        if nums[i] > max_n:
            max_n = nums[i]

        # 최소값
        elif nums[i] < min_n:
            min_n = nums[i]

    print(f'#{test_case} {max_n - min_n}')
