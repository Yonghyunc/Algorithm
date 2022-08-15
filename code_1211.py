# 1211. [S/W 문제해결 기본] 2일차 - Ladder2
# 8/13
# 개인적인 도전


import sys

sys.stdin = open('input_ladder2.txt')


for _ in range(10):

    # 테스트케이스 번호
    t = int(input())

    ladder = [0] * 100

    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    # 좌우만 고려
    dy = [-1, 1]

    # 모든 이동거리 넣을 리스트
    move_all = []

    # 출발점 전부 실행
    for start_num in range(100):
        x = 1  # 상하
        y = start_num  # 좌우
        move = 1  # 이동거리

        while True:

            # 좌우 이동 확인
            for d in dy:
                y = y + d

                # 인덱스 범위 넘어가지 않도록
                while True:
                    if 0 <= y < 100 and ladder[x][y] == 1:
                        dir = d
                        y = y + dir
                        move += 1
                    else:
                        x += 1
                        break

            else:
                move += 1
                x += 1

            # 이동 거리 리스트에 저장
            if x == 99:
                move_all.append(move)
                break

        min_move = move_all[0]
        for i in range(len(move_all)):
            if min_move > move_all[i]:
                min_move = move_all[i]
                min_idx = i

    print(f'#{t} {min_idx}')
