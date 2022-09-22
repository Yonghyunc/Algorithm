# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금


def exchange(depth, val):
    global bonus

    # 교환을 끝마쳤을 때, 가장 큰 보너스를 찾는다
    if depth == change:
        # print(numbers)
        for k in range(n):
            val += int(numbers[k]) * (10 ** (n - k - 1))
        if bonus < val:
            bonus = val
        return

    # 가지치기
    if depth == change - 1:
        if int(numbers[0]) < int(num_sorted[0]) and int(numbers[1]) < int(num_sorted[1]):
            return

    if depth == change - 2:
        if int(numbers[0]) < int(num_sorted[0]) and int(numbers[1]) < int(num_sorted[1]) and int(numbers[2]) < int(num_sorted[2]):
            return

    depth += 1
    for i in range(n):
        for j in range(i, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            exchange(depth, val)
            numbers[j], numbers[i] = numbers[i], numbers[j]


for tc in range(1, int(input()) + 1):
    num, change = input().split()
    change = int(change)                    # 교환 횟수
    n = len(num)                            # 숫자의 자릿수
    numbers = [num[i] for i in range(n)]    # 리스트로 저장한 숫자판 정보

    num_sorted = sorted(numbers, reverse=True)
    bonus = 0
    exchange(0, 0)
    print(f'#{tc} {bonus}')