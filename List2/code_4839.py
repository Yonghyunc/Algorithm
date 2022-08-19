# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색
# 8/11

t = int(input())

for test_case in range(1, t + 1):

    p, a, b = map(int, input().split())

    case = [a, b]
    count_ab = []

    for i in case:

        count = 1  # 탐색 횟수
        l = 1  # 검색 구간의 왼쪽
        r = p  # 검색 구간의 오른쪽
        mid = int((l + r) / 2)  # 중간 페이지

        while True:
            if i < mid:
                r = mid
                mid = int((l + r) / 2)
                count += 1

            elif i > mid:
                l = mid
                mid = int((l + r) / 2)
                count += 1

            else:
                break

        count_ab.append(count)

    # 더 먼저 찾은 쪽을 출력
    if count_ab[0] < count_ab[1]:
        print(f'#{test_case} A')
    elif count_ab[0] > count_ab[1]:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')


# 재귀함수로도 풀 수 있음!!
# 모든 반복문은 재귀함수로 풀 수 있고, 모든 재귀함수는 반복문으로 풀 수 있다!!
# int((l + r) / 2) == (l + r) // 2
