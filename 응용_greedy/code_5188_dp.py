# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
# DP(메모리제이션) 풀이

for tc in range(1, int(input()) + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    memo = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 1. 원래 리스트의 값을 더한다
            memo[i][j] += matrix[i][j]

            if i == 0 and j == 0:
                continue

            # 2. 위, 왼쪽을 더해서 최소합으로 갱신
            if i == 0:                          # 가로 맨 윗줄이라면,
                memo[i][j] += memo[i][j - 1]    # 왼쪽의 값을 더해줌
            elif j == 0:                        # 세로 맨 왼쪽 줄이라면,
                memo[i][j] += memo[i - 1][j]    # 위쪽의 값을 더해줌

            else:
                memo[i][j] += min(memo[i][j - 1], memo[i - 1][j])   # 위쪽, 왼쪽 값 중 더 작은 값을 더해줌

        print(f'#{tc} {memo[n - 1][n - 1]}')