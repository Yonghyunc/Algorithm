# 백준 2564 : 경비원

w, h = map(int, input().split())
n = int(input())
stores = [list(map(int, input().split())) for _ in range(n)]

# 동근이 위치를 리스트의 가장 처음에 넣어줌
stores.insert(0, list(map(int, input().split())))

# 좌표처럼 표현
for i in range(n + 1):
    if stores[i][0] == 1:           # 북 [0, _]
        stores[i][0] = 0
    elif stores[i][0] == 2:         # 남 [h, _]
        stores[i][0] = h
    elif stores[i][0] == 3:         # 서 [_, 0]
        stores[i][0] = stores[i][1]
        stores[i][1] = 0
    elif stores[i][0] == 4:         # 동 [_, w]
        stores[i][0] = stores[i][1]
        stores[i][1] = w
print(stores)
dis = 0
for i in range(1, n + 1):

    # 동근이와 상점이 같은 방향에 위치할 때는 위치의 차만 구해줌
    if stores[0][0] == stores[i][0]:
        dis += abs(stores[0][1] - stores[i][1])

    else:
        # 동근이와 상점의 x좌표 위치의 합이 높이보다 작을 때,
        if stores[0][0] + stores[i][0] <= h:
            dis += stores[0][0] + stores[i][0]
        else:
            dis += 2 * h - (stores[0][0] + stores[i][0])

        if stores[0][1] + stores[i][1] <= w:
            dis += stores[0][1] + stores[i][1]
        else:
            dis += 2 * w - (stores[0][1] + stores[i][1])

    print(dis)
