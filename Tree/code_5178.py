# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합


def post_sum(k):
    if 2 * k + 1 <= n:
        a = post_sum(2 * k)
        b = post_sum(2 * k + 1)
        tree[k] = a + b
    elif 2 * k == n:            # 자식노드가 1개인 경우 (마지막 리프노드)
        a = post_sum(2 * k)
        tree[k] = a
    return tree[k]


for tc in range(1, int(input()) + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)
    for _ in range(m):
        i, x = map(int, input().split())
        tree[i] = x

    post_sum(1)

    print(f'#{tc} {tree[l]}')