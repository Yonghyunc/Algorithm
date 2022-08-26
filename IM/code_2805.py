# 2805. 농작물 수확하기

for test_case in range(1, int(input()) + 1):
    n = int(input())
    farm = [list(map(int, (map(' '.join, input())))) for _ in range(n)]

    # 전체 농장 수확량
    whole = 0
    for i in range(n):
        for j in range(n):
            whole += farm[i][j]

    # 마름모 가운데 줄
    center = n // 2 + 1

    # 마름모를 제외한 구역의 수확량
    minus = 0

    # 마름모 위쪽
    cut = n // 2
    for i in range(center - 1):
        for j in range(cut):
            minus += farm[i][j]
            minus += farm[i][- j - 1]
        cut -= 1

    # 마름모 아래쪽
    cut = n // 2
    for i in range(n - 1, center - 1, -1):
        for j in range(cut):
            minus += farm[i][j]
            minus += farm[i][- j - 1]
        cut -= 1

    print(f'#{test_case} {whole-minus}')