# 백준 2667. 단지번호붙이기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, cnt):
    visited[x][y] = True        # 시작 집 방문 표시
    queue = [[x, y]]            # queue 에 삽입

    while queue:
        x, y = queue.pop(0)
        cnt += 1                # 집의 수 카운트
        for d in range(4):      # 델타이동
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:         # 델타이동한 x, y 값이 배열의 범위 내에 있고
                if arr[nx][ny] == 1 and not visited[nx][ny]:    # 방문하지 않은 집이 있을 때,
                    visited[nx][ny] = True                      # 방문 체크하고
                    queue.append([nx, ny])                      # queue 에 삽입
    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]       # 방문 여부
group = []                                      # 단지별 속하는 집의 수를 담을 리스트

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:    # 방문하지 않은 집이면
            group.append(bfs(i, j, 0))              # bfs 함수 실행
group.sort()                                        # 오름차순으로 정렬
print(len(group), *group, sep='\n')                 # 한 줄에 하나씩 출력