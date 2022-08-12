# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
# 8/11

t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    # 집합 a
    a = list(range(1, 13))
    al = len(a)

    # 모든 부분집합을 담을 리스트
    subset = [[0] for _ in range(1 << al)]

    for i in range(1 << al):
        sub = []
        for j in range(al):
            if i & (1 << j):
                sub.append(a[j])
        subset[i] = sub

    # 부분집합의 원소의 개수를 담을 리스트
    subset_num = []

    for i in range(len(subset)):
        num = 0
        for j in range(len(subset[i])):
            num += 1
        subset_num.append(num)

    # 각 부분집합의 합을 담을 리스트
    subset_sum = []

    for i in range(len(subset)):
        sum = 0
        for j in range(len(subset[i])):
            sum += subset[i][j]
        subset_sum.append(sum)

    # 조건에 맞는 경우 찾기
    both = 0
    for i in range(len(subset)):
        if subset_num[i] == n and subset_sum[i] == k:
            both += 1

    print(f'#{test_case} {both}')
