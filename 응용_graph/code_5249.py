# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

def find_set(n):
    if n != parents[n]:
        parents[n] = find_set(parents[n])
    return parents[n]


for tc in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    tree = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        tree.append([c, a, b])
    tree.sort()
    parents = list(range(v + 1))
    cost = 0
    cnt = 0

    for i in range(e):
        root_x = find_set(tree[i][1])
        root_y = find_set(tree[i][2])
        if root_x != root_y:
            cnt += 1
            cost += tree[i][0]
            parents[root_y] = root_x
        if cnt == v:
            break

    print(f'#{tc} {cost}')





