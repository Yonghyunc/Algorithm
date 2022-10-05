# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

from heapq import heappush, heappop

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(x, y):
    distance[x][y] = 0
    heap = [(0, x, y)]         # 비용, x좌표, y좌표

    while heap:
        min_dist, min_x, min_y = heappop(heap)

        if min_dist > distance[min_x][min_y]:   # 최소 비용을 넘어서면 지나감
            continue

        for d in range(4):                      # 델타이동
            nx = min_x + dx[d]
            ny = min_y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:                 # 이동한 좌표가 범위 내
                if arr[nx][ny] - arr[min_x][min_y] < 0:     # 높이 차이가 음수일 때는
                    diff = 0                                # 추가 연료 소비량 == 0
                else:
                    diff = arr[nx][ny] - arr[min_x][min_y]

                new_dist = distance[min_x][min_y] + 1 + diff    # 새로운 비용

                if new_dist < distance[nx][ny]:                 # 새로운 비용이 최소 비용보다 작다면
                    distance[nx][ny] = new_dist                 # 최소 비용 갱신
                    heappush(heap, (new_dist, nx, ny))          # 비용, x좌표, y좌표를 힙에 넣어줌


for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    INF = 999999999
    distance = [[INF] * n for _ in range(n)]

    dijkstra(0, 0)
    print(f'#{tc} {distance[n - 1][n - 1]}')