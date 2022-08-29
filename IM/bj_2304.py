# 백준 2304 : 창고 다각형


n = int(input())        # 기둥 개수
bar = [list(map(int, input().split())) for _ in range(n)]

# 위치 순으로 정렬
for _ in range(n - 1):
    for i in range(n - 1):
        if bar[i][0] > bar[i + 1][0]:
            bar[i], bar[i + 1] = bar[i + 1], bar[i]

# 최대 높이와, 그 값의 인덱스 찾기
max_height = 0
max_idx = 0
for i in range(n):
    if max_height < bar[i][1]:
        max_height = bar[i][1]
        max_idx = i

area = 0

# 최대 높이 기둥 오른쪽 넓이
now_idx = bar[0][0]
now_height = bar[0][1]
for i in range(1, max_idx + 1):
    if now_height <= bar[i][1]:
        area += now_height * (bar[i][0] - now_idx)
        now_height = bar[i][1]
        now_idx = bar[i][0]


# 최대 높이 기둥 넓이
area += max_height


# 최대 높이 기둥 왼쪽 넓이
now_idx = bar[-1][0]
now_height = bar[-1][1]
for i in range(n - 1, max_idx - 1, -1):
    if now_height <= bar[i][1]:
        area += now_height * (now_idx - bar[i][0])
        now_height = bar[i][1]
        now_idx = bar[i][0]

print(area)