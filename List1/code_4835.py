# 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합
# 8/9


# 테스트 케이스 수
t = int(input())

for test_case in range(1, t + 1):

    # 정수 개수, 구간 개수
    n, m = map(int, input().split())

    # n개의 정수
    nums = list(map(int, input().split()))

    # 모든 이웃한 M개 합을 담을 리스트 생성
    num_sums = []

    for i in range(n - m + 1):

        # 개별 이웃한 M개 합
        num_sum = 0
        for j in range(m):
            num_sum += nums[i + j]
        num_sums.append(num_sum)

    # 모든 이웃한 M개 합을 담은 리스트 정렬
    num_sums_sort = sorted(num_sums)

    print(f'#{test_case} {num_sums_sort[-1]-num_sums_sort[0]}')


'''
sliding window

합은 최초 한번만 구함 -- 그 다음부터는 앞에꺼 빼고 뒤에꺼 더하고
'''
