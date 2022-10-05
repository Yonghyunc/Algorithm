# 1861. 정사각형 방


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):

    n = int(input())    # 방의 길이
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_move = 1
    min_start = 10 ** 3

    # 각 시작점 별로 이동거리 계산
    for x in range(n):
        for y in range(n):
            start = arr[x][y]
            move = 1

            # 이동할 수 있을 때까지 계속 이동
            while True:
                for i in range(4):
                    if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n:       # 범위 내
                        if arr[x + dx[i]][y + dy[i]] == arr[x][y] + 1:  # 값이 +1
                            x = x + dx[i]
                            y = y + dy[i]
                            move += 1
                            break
                else:
                    # 이동거리가 최대 이동거리보다 크면, 최대 이동거리와 시작 값 갱신
                    if max_move < move:
                        max_move = move
                        min_start = start
                    # 이동거리가 최대 이동거리와 같으면, 시작 값 비교 후 갱신
                    elif max_move == move:
                        if start < min_start:
                            min_start = start

                    break

    print(f'#{tc} {min_start} {max_move}')