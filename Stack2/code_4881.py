# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
# 8/23
# 결과는 나오지만 제한시간 초과...


def number(choice, start):
    global min_sum
    global cho_sum

    if cho_sum > min_sum:
        return

    if len(choice) == n:
        if min_sum > cho_sum:
            min_sum = cho_sum
        return

    for i in range(n):
        for j in range(start, n):
            if not visited_x[i] and not visited_y[j]:
                visited_x[i] = True
                visited_y[j] = True
                choice.append(arr[i][j])
                cho_sum += arr[i][j]

                number(choice, j + 1)

                visited_x[i] = False
                visited_y[j] = False
                choice.pop()
                cho_sum -= arr[i][j]


for test_case in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited_x = [False] * n   # 행만 확인
    visited_y = [False] * n
    choice = []
    min_sum = 1000000
    cho_sum = 0
    number([], 0)
    print(f'#{test_case} {min_sum}')
