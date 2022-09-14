# 4613. 러시아 국기 같은 깃발

color = ["W", "B", "R"]
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]

    print(board)

    cnt = [0] * 3  # 각 색상 라인의 개수 (흰색 줄, 파란색 줄이 한 개 이상인지 확인용)
    paint = 0  # 칠해야 하는 횟수

    for i in range(n):  # 행의 개수만큼 반복
        col = []
        for c in color:
            col.append(board[i].count(c))
        print(col)

        if cnt[0] < 1:  # 흰색 줄이 하나도 없을 때,
            paint += m - col[0]  # 나머지 색깔을 흰색 줄로 바꿔줌
            cnt[0] += 1

        elif cnt[1] < 1:  # 파란 줄이 하나도 없을 때,
            if col[0] >= col[1] and n - (i + 1) > 2:  # 흰색이 더 많고, 남은 줄이 두 줄 초과일 때
                paint += m - col[0]
            else:  # 파란색이 더 많거나, 남은 줄이 두 줄 이하일 때
                paint += m - col[1]
                cnt[1] += 1

        else:  # 최소 하나씩의 흰색 줄, 파란색 줄이 있을 때
            if col[1] >= col[2] and n - (i + 1) >= 1:  # 파란색이 더 많고, 남은 줄이 있을 때
                paint += m - col[1]
            else:  # 빨간색이 더 많거나, 남은 줄이 단 한 줄일 때
                paint += m - col[2]
        print(i, '/', paint)
    print(paint)
