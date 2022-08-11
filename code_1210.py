# 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# 8/11

import sys

sys.stdin = open("input.txt")

import copy

for _ in range(10):
    test_case = int(input())

    data = [0] * 100

    for i in range(100):
        data[i] = list(map(int, input().split()))

    # 좌우만 고려
    side = [1, -1]

    # 출발점
    start_num = 0

    for start in range(100):

        # 깊은 복사 이용하여 반복 시마다 데이터 값 리셋
        data_copy = copy.deepcopy(data)

        # 출발 위치
        idx = 0
        idy = start

        # 제일 아래에 도착할 때까지 반복
        while True:

            for s in side:

                # 좌우 인덱스 범위 넘어가지 않으며, 칸의 값이 1일 때
                if 0 <= idy + s <= 99:
                    print(idx, idy)
                    if data_copy[idx][idy + s] == 1:

                        data_copy[idx][idy] = 0  # 지나온 값은 돌아가지 않도록 0으로 변환
                        idy = idy + s  # y인덱스 변경
                        break

            else:
                idx += 1

            if idx == 99:
                print(data_copy[idx][idy])
                break

        if data_copy[99][idy] == 2:
            start_num = start

    print(f'#{test_case} {start_num}')
