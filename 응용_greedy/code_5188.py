# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합


def move(x, y):
    global num
    global min_num

    if num > min_num:          # 최소값을 넘으면 그 경로는 가지 않음
        return

    num += arr[x][y]            # 현재 판의 숫자를 더해줌

    if x < n - 1:
        move(x + 1, y)          # 아래로 이동

    if y < n - 1:
        move(x, y + 1)          # 오른쪽으로 이동

    if x == n - 1 and y == n - 1:       # 마지막 지점에 도착하면
        if num < min_num:               # 최소값과 비교하여, 더 작으면
            min_num = num               # 최소값을 갱신해줌

    num -= arr[x][y]                    # 이전 재귀로 돌아가며 현재 판의 숫자를 빼줌


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    num = 0
    min_num = 13*13*10

    move(0, 0)
    print(f'#{tc} {min_num}')
