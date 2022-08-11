# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
# 8/11
# list 이용

t = int(input())

for test_case in range(1, t + 1):

    box = int(input())

    red = []  # 기존에 리스트로 작성
    blue = []
    num = 0

    for _ in range(box):
        x1, y1, x2, y2, c = map(int, input().split())

        # red
        if c == 1:
            for i in range(x2 - x1 + 1):
                for j in range(y2 - y1 + 1):
                    red.append([x1 + i, y1 + j])  # 리스트이기 때문에 append 메서드 활용

        # blue
        if c == 2:
            for i in range(x2 - x1 + 1):
                for j in range(y2 - y1 + 1):
                    blue.append([x1 + i, y1 + j])

    # 들여쓰기 조정 후
    for b in range(len(red)):
        if red[b] in blue:
            num += 1

    print(f'#{test_case} {num}')
