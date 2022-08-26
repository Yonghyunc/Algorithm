# 6190. 정곤이의 단조 증가하는 수

for test_case in range(1, int(input()) + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    # 나올 수 있는 모든 두 수의 곱 찾기
    numbers = []
    for i in range(n):
        for j in range(i + 1, n):
            numbers.append(nums[i] * nums[j])

    # 숫자를 문자로 변경하여 단조 증가 여부를 살펴보고, 단조 증가할 시 리스트에 넣어줌
    # 한 자리의 경우 단조 증가로 포함
    mono_list = []
    for num in numbers:
        mono = True
        num = str(num)
        for i in range(len(str(num)) - 1):
            if int(num[i]) > int(num[i + 1]):
                mono = False
        if mono:
            mono_list.append(int(num))

    # for num in numbers:
    #     if num >= 10000:
    #         if num % 10 >= num // 10 >= num // 100 >= num // 1000 >= num // 10000:
    #             mono.append(num)
    #     if num >= 1000:
    #         if num % 10 >= num // 10 >= num // 100 >= num // 1000:
    #             mono.append(num)
    #     if num >= 100:
    #         if num % 10 >= num // 10 >= num // 100:
    #             mono.append(num)
    #     if num >= 10:
    #         if num % 10 >= num // 10:
    #             mono.append(num)

    # 가장 큰 단조 증가 수 찾음
    max_mono = -1
    for i in range(len(mono_list)):
        if mono_list[i] > max_mono:
            max_mono = mono_list[i]

    print(f'#{test_case} {max_mono}')