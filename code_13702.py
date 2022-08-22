# 13702. 델타 검색


for test_case in range(1, 11):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 총합
    all_sum = 0

    # 각 좌표와 인접값과의 차의 절댓값의 합을 구함
    for i in range(n):
        for j in range(n):
            delta_sum = 0
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                # 인덱스 범위 내에 위치
                if 0 <= x < n and 0 <= y < n:
                    delta_sum += abs(arr[i][j] - arr[x][y])
            all_sum += delta_sum

    print(f'#{test_case} {all_sum}')



