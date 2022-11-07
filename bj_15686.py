# 백준 15686. 치킨 배달

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# print(city)

# 치킨집과 집 좌표
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
# print(chicken)
# print(house)

distance = []
for hx, hy in house:
    dis = []
    for cx, cy in chicken:
        dis.append(abs(cx - hx) + abs(cy - hy))
    distance.append(dis)
# print(distance)

min_dis = []
min_idx = []
for i in range(len(distance)):
    min_idx.append(distance[i].index(min(distance[i])))
    min_dis.append(min(distance[i]))

print(min_dis)
print(min_idx)

if m >= len(chicken):
    print('answer', sum(min_dis))
else:
    sum_dis = [0] * (max(min_idx) + 1)
    for i in range(len(min_dis)):
        sum_dis[min_idx[i]] += min_dis[i]
    print(sum_dis)
# 무엇을 고민해야 하느냐
# 복수의 치킨집 해결법
# 하나의 치킨집 해결법