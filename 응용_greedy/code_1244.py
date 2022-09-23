# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금


def exchange(depth, numbers):
    global bonus
    val = int("".join(numbers))         # 숫자로 변환

    # 교환을 끝마쳤을 때, 가장 큰 보너스를 찾는다
    if depth == change:
        if bonus < val:
            bonus = val
        return

    # 가지치기
    # depth 별로 이미 나온 배열은 검사하지 않음!!
    if val in d_case[depth]:
        return

    d_case[depth].append(val)           # depth 별로 숫자 배열 저장 (중복 검사 하지 않기 위해)

    # 교환 실행
    for i in range(n - 1):
        for j in range(i + 1, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            exchange(depth + 1, numbers)
            numbers[j], numbers[i] = numbers[i], numbers[j]


for tc in range(1, int(input()) + 1):
    num, change = input().split()
    change = int(change)                    # 교환 횟수
    n = len(num)                            # 숫자의 자릿수
    numbers = [num[i] for i in range(n)]    # 리스트로 저장한 숫자판 정보

    d_case = [[] for _ in range(change)]    # 같은 depth 중복 검사
    bonus = 0
    exchange(0, numbers)
    print(f'#{tc} {bonus}')
