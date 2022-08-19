# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
# 8/11


t = int(input())

for test_case in range(1, t + 1):

    # 정수의 개수
    n = int(input())

    # n개의 정수
    nums = list(map(int, input().split()))

    # 오름차순으로 정렬
    for _ in range(len(nums) - 1):  # 모두 다 정렬될 때까지 반복
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    # 길이가 10인 빈 리스트 생성
    special = [0] * 10

    for i in range(10):

        # 짝수 인덱스에는 가장 큰 수부터
        if i % 2 == 0:
            special[i] = nums[-(i // 2 + 1)]

        # 홀수 인덱스에는 가장 작은 수부터
        else:
            special[i] = nums[i // 2]

    print(f'#{test_case}', end=' ')
    print(*special)

    # print(f'#{test_case}', *special)
