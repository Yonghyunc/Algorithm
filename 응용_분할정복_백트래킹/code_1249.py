# 1249. [S/W 문제해결 응용] 4일차 - 보급로

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# def bfs(x, y, work):
#     global min_work
#
#     if x == n - 1 and y == n - 1:
#         if min_work > work:
#             min_work = work
#         return min_work
#
#     visited[x][y] = True
#
#     if dp[x][y] == 0 or work < dp[x][y]:
#         dp[x][y] = work
#
#     for d in range(4):
#         if 0 <= x + dx[d] < n and 0 <= y + dy[d] < n:
#             if not visited[x + dx[d]][y + dy[d]]:
#                 work = dp[x][y] + arr[x + dx[d]][y + dy[d]]
#                 if work >= min_work:
#                     pass
#                 else:
#                     visited[x + dx[d]][y + dy[d]] = True
#                     bfs(x + dx[d], y + dy[d], work)
#     visited[x][y] = False


def bfs(x, y, dp):
    if x == n - 1 and y == n - 1:
        return dp

    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if 0 < dp[nx][ny] < dp[x][y] + arr[nx][ny]:
                pass
            if not visited[nx][ny]:
                dp[nx][ny] = dp[x][y] + arr[nx][ny]
                print('nx:', nx, 'ny:', ny, 'dp', dp[nx][ny])
                bfs(nx, ny, dp)


# for tc in range(1, int(input()) + 1):
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
print(arr)
visited = [[False] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]
min_work = n * n * 9
bfs(0, 0, dp)
print(dp)
print(dp[n-1][n-1])