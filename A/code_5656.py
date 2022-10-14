# 5656. [모의 SW 역량테스트] 벽돌 깨기

'''
블럭을 깬 다음에 내려줘야 함.... 아놔


'''
# 하, 상, 좌, 우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]


def dfs(n):
    global min_brick

    if n < 0:
        brick = 0
        for w in range(width):
            for h in range(height):
                if beads[w][h] > 0:
                    brick += 1
        if brick < min_brick:
            min_brick = brick
        return

    for w in range(width):                  # 구슬 어디에 떨어뜨릴까
        for h in range(height):             # 벽돌이 있는 곳
            if beads[h][w] > 0 and [h, w] not in used:
                if beads[h][w] != 1:
                    crush(h, w, beads[h][w])
                dfs(n - 1)
                if beads[h][w] != 1:
                    crush_restore(h, w, beads[h][w])
                break


def crush(h, w, v):
    used.append([h, w])
    for d in range(4):
        for r in range(1, v):
            if 0 <= h + dh[d] * r < height and 0 <= w + dw[d] * r < width:
                if beads[h + dh[d] * r][w + dw[d] * r] == 1:
                    beads[h + dh[d] * r][w + dw[d] * r] = -1
                elif beads[h + dh[d] * r][w + dw[d] * r] > 1 and [h + dh[d] * r, w + dw[d] * r] not in used:
                    crush(h + dh[d] * r, w + dw[d] * r, beads[h + dh[d] * r][w + dw[d] * r])


def crush_restore(h, w, v):
    used.remove([h, w])
    for d in range(4):
        for r in range(1, v):
            if 0 <= h + dh[d] * r < height and 0 <= w + dw[d] * r < width:
                if beads[h + dh[d] * r][w + dw[d] * r] == -1:
                    beads[h + dh[d] * r][w + dw[d] * r] = 1
                elif beads[h + dh[d] * r][w + dw[d] * r] > 1 and [h + dh[d] * r, w + dw[d] * r] in used:
                    crush_restore(h + dh[d] * r, w + dw[d] * r, beads[h + dh[d] * r][w + dw[d] * r])


# for tc in range(1, int(input()) + 1):
n, width, height = map(int, input().split())     # 구슬 개수, W X H 배열

beads = [list(map(int, input().split())) for _ in range(height)]
used = []
min_brick = width * height
dfs(n)
print(min_brick)