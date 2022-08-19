# 1949. [모의 SW 역량테스트] 등산로 조성


t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    print(board)

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def dfs(x, y, cut):
#     global course
#     now = board[x][y]   # 현재 위치

#     for v in range(4):
#         x1 = x + dx[v]
#         y1 = y + dy[v]

#         # 인덱스 범위 내 지나간 적 없는 곳
#         if 0 <= x1 < n and 0 <= y1 < n and not trail[x1][y1]:

#             # 현재 위치보다 낮으면 go
#             if board[x1][y1] < now:
#                 trail[x1][y1] = True
#                 course += 1
#                 dfs(x1, y1, cut)

#             # 현재 위치와 같거나 더 높으면 cut
#             # cut 은 단 한번만 시행
#             else:
#                 if board[x1][y1] - cut < now:
#                     cut = 0
#                     trail[x1][y1] = True
#                     course += 1
#                     dfs(x1, y1, cut)


# n = 3
# k = 2

# board = [list(map(int, input().split())) for _ in range(n)]
# trail = [[False] * n for _ in range(n)]


# all_course = []
# course = 0

# for max_height in range(20, 0, -1):
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] == max_height:       # 높은 봉우리부터 검사
#                 course = 1
#                 trail[i][j] = True
#                 dfs(i, j, k)
#                 all_course.append(course)
# print(all_course)
