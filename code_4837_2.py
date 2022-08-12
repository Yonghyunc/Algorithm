# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

# 코드 피드백 후 수정

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

    both = 0

    # 부분집합의 원소의 개수와 부분집합의 합을 한번에 계산
    for i in range(len(subset)):
        num = 0
        sum = 0
        for j in range(len(subset[i])):
            num += 1
            sum += subset[i][j]

        # 조건 충족 여부 확인
        if num == n and sum == k:
            both += 1

    print(f'#{test_case} {both}')
