# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
# 8/11
# set 이용

t = int(input())

for test_case in range(1, t + 1):

    box = int(input())

    red = {0}  # 중복 없애기 위해 set으로 받음
    blue = []
    num = 0  # 보라색 박스의 수

    for _ in range(box):
        x1, y1, x2, y2, c = map(int, input().split())

        # red
        if c == 1:
            for i in range(x2 - x1 + 1):
                for j in range(y2 - y1 + 1):
                    red.add((x1 + i, y1 + j))

        # blue
        if c == 2:
            for i in range(x2 - x1 + 1):
                for j in range(y2 - y1 + 1):
                    blue.append((x1 + i, y1 + j))

    # 겹치는 박스 확인
    red = list(red)  # 포함 여부 확인 위해 list로 변환
    for b in range(len(red)):
        if red[b] in blue:
            num += 1

    print(f'#{test_case} {num}')
