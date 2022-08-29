n = int(input())
bar = [list(map(int, input().split())) for _ in range(n)]

# 1) 정렬
highest = bar[0][1]
for _ in range(n):
    for i in range(n - 1):
        if bar[i][0] > bar[i + 1][0]:
            bar[i], bar[i + 1] = bar[i + 1], bar[i]
        if highest < bar[i + 1][1]:
            highest = bar[i + 1][1]
            high_idx = i + 1

print(highest) # 10
print(high_idx)  # 3

print(bar)  #[[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

# 2) for문

block = 0

# 가장 높은 곳 기준 왼쪽
for i in range(high_idx):
    if bar[i][1] < bar[i + 1][1]:   # 오른쪽이 더 크면
        now_height = bar[i][1]
        now_locate = bar[i][0]
        block += now_height * (bar[i + 1][0] - now_locate)

    else:
        now_height = bar[i][1]
        now_locate = bar[i][0]

print(block)


#     if stack1[-1] < bar[i][1]:
#         stack1.append(bar[i][1])        # 높이
#         stack2.append(bar[i][0])        # 위치
#
# # 가장 높은 곳 기준 오른쪽 끝부터
# for i in range(n - 1, high_idx, -1):
#     if stack1[-1] > bar[i][1]:
#         stack1.append(bar[i][1])        # 높이
#         stack2.append(bar[i][0])        # 위치

