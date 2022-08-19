# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

# 코드 피드백 후 수정


def color(x1, x2, y1, y2):
    color = []

    for i in range(x2 - x1 + 1):
        for j in range(y2 - y1 + 1):
            color.append([x1 + i, y1 + j])

    return color


t = int(input())

for test_case in range(1, t + 1):

    box = int(input())

    red = []
    blue = []
    num = 0

    for _ in range(box):
        x1, y1, x2, y2, c = map(int, input().split())

        # red
        if c == 1:
            red += color(x1, x2, y1, y2)

        # blue
        if c == 2:
            blue += color(x1, x2, y1, y2)

    # 들여쓰기 조정 후
    for b in range(len(red)):
        if red[b] in blue:
            num += 1

    print(f'#{test_case} {num}')
