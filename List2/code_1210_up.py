# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# 8/11
# 12일에 다시 도전


import sys

sys.stdin = open("input.txt")

for _ in range(10):

    t = int(input())

    data = [0] * 100

    for i in range(100):
        data[i] = list(map(int, input().split()))

    # 좌, 우
    dy = [-1, 1]

    # 출발점
    start = -1

    # 비교는 밑에서 두번째 줄부터 시작 (맨 아래에서는 양옆으로 이동 X)
    nowx = 98

    for i in range(100):
        for j in range(100):
            if data[99][j] == 2:
                nowy = j

    while True:

        for s in range(2):
            if 0 <= nowy + dy[s] < 100:
                if data[nowx][nowy + dy[s]] == 1:
                    data[nowx][nowy] = 0  # 지나온 값은 돌아가지 않도록 0으로 변환
                    nowy = nowy + dy[s]
                    break

        else:
            nowx = nowx - 1

        if nowx == 0:
            start = nowy
            break

    print(f'#{t} {start}')
