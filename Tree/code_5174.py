# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree


def find_node(n):
    global cnt
    for i in range(e):
        if arr[2 * i] == n:
            cnt += 1
            find_node(arr[2 * i + 1])


for tc in range(1, int(input()) + 1):

    # e : 간선의 개수, n : 서브 트리의 루트 노드
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 1

    find_node(n)

    print(f'#{tc} {cnt}')



