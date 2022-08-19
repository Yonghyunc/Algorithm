# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# 8/9


## 풀이 1


for test_case in range(1, 11):
    dump = int(input())
    nums = list(map(int, input().split()))

    a = 100

    for n in range(dump):

        # 주어진 덤프 횟수 내 평탄화 완료
        if a <= 1:
            break

        # 오름차순으로 정렬
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        # 덤프
        nums[-1] -= 1
        nums[0] += 1

    # 오름차순으로 정렬
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

    # 최고점과 최저점의 차이
    diff = nums[-1] - nums[0]

    print(f'#{test_case} {diff}')


# -----------------------------------------------------
## 풀이 2

'''
정렬 -> 함수로 만드는 방법 !
'''

# 오름차순으로 정렬하는 함수 선언
def sort_num(x):
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]


for test_case in range(1, 11):
    dump = int(input())
    nums = list(map(int, input().split()))

    a = 100

    for n in range(dump):

        # 주어진 덤프 횟수 내 평탄화 완료
        if a <= 1:
            break

        # 오름차순으로 정렬
        sort_num(nums)

        # 덤프
        nums[-1] -= 1
        nums[0] += 1

    # 오름차순으로 정렬
    sort_num(nums)

    # 최고점과 최저점의 차이
    a = nums[-1] - nums[0]

    print(f'#{test_case} {a}')
