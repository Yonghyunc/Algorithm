# 1949. [모의 SW 역량테스트] 등산로 조성


t = int(input())

for test_case in range(1, t + 1):
    n, k = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    print(board)