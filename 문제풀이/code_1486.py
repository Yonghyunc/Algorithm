# 1486. 장훈이의 높은 선반

for tc in range(1, int(input()) + 1):
    n, b = map(int, input().split())  # n : 직원 수 / b : 탑의 높이
    clerk = list(map(int, input().split()))

    min_height = 10000 * n

    # 비트연산자 이용하여 부분집합의 합 구하기
   for i in range(1 << len(clerk)):
        height = 0
        for j in range(len(clerk)):
            if i & (1 << j):
                height += clerk[j]

        # 선반보다 높은 탑 중 가장 낮은 탑
        if b <= height < min_height:
            min_height = height

    print(f'#{tc} {min_height - b}')


# --------------- 때가 되면 재귀로도 한 번...---------


def plus(clerk, k):
    global height
    global min_height

    if k == n:
        return min_height

    if height <= b:
        height += clerk[k]
        print("k: ", clerk[k], " / h: ", height)
        plus(clerk, k + 1)
        nothing(clerk, k + 1)

    if height < min_height:
        min_height = height


def nothing(clerk, k):
    if k == n:
        return min_height
    plus(clerk, k + 1)
    nothing(clerk, k + 1)
