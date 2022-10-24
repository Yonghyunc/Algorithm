# 백준 16236. 아기 상어

from collections import deque

n = int(input())

sea = [list(map(int, input().split())) for _ in range(n)]
print(sea)

for x in range(n):              # 상어의 위치 찾음
    for y in range(n):
        if sea[x][y] == 9:
            sx, sy = x, y

sea[sx][sy] = 0                 # 상어의 처음 위치를 찾고 난 후에는 그 자리를 0으로 표시


shark = 2                       # 아기 상어 처음 크기
fish_cnt = 0                    # 먹은 물고기 수
time_cnt = 0                    # 아기 상어가 혼자 물고기를 잡아 먹는 시간

# 상, 좌, 하, 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

find_queue = deque()                 # 이동 가능한 좌표


visited = [[False] * n for _ in range(n)]       # 확인 여부
find_queue.append((sx, sy, 0))                  # 현재 상어의 위치 추가

while find_queue:                               # 이동 가능한 좌표가 있을 때,
    nx, ny, dis = find_queue.popleft()          # 하나씩 꺼내서 (우선순위 순)
    visited[sx][sy] = True                      # 확인여부 체크하고

    for d in range(4):
        if 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < n:     # 범위 내
            if not visited[nx + dx[d]][ny + dy[d]]:         # 아직 확인 안한

                if sea[nx + dx[d]][ny + dy[d]] == 0 or sea[nx + dx[d]][ny + dy[d]] == shark:    # 통과 가능한 곳
                    find_queue.append((nx + dx[d], ny + dy[d], dis + 1))                        # find_queue 에 넣어줌
                    visited[nx + dx[d]][ny + dy[d]] = True

                elif 0 < sea[nx + dx[d]][ny + dy[d]] < shark:       # 먹을 수 있는 물고기
                    fish_cnt += 1                                   # 먹은 물고기 수 + 1
                    time_cnt += dis + 1                             # 이동거리(시간) 추가
                    sx = nx + dx[d]                                 # 상어 위치 갱신
                    sy = ny + dy[d]
                    sea[sx][sy] = 0                                 # 물고기 위치는 0으로 갱신
                    print(sx, sy, time_cnt)
                    find_queue = deque()                            # find_queue 비워서 while 문 종료
                    find_queue.append((sx, sy, 0))
                    visited = [[False] * n for _ in range(n)]
                    break

                print(find_queue)
        if fish_cnt == shark:       # 상어 크기만큼 물고기를 먹었으면
            shark += 1              # 진화
            fish_cnt = 0

        if fish_cnt == 4:
            break
print(sea)
print(shark)
print(time_cnt)


