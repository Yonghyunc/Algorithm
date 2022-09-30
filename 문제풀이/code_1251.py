# 1251. [S/W 문제해결 응용] 4일차 - 하나로

from heapq import heappush, heappop


def prim(s):
    visited = [False] * n
    heap = [(0, s)]
    cost = 0

    while heap:
        min_cost, min_node = heappop(heap)

        if visited[min_node]:       # 방문했다면 넘어감
            continue

        visited[min_node] = True    # 방문처리
        cost += min_cost

        for i in range(1, n):
            if not visited[i]:      # 방문하지 않았다면, 환경 부담금 계산하여 힙에 삽입
                now_cost = e * ((arr[min_node][0] - arr[i][0]) ** 2 + (arr[min_node][1] - arr[i][1]) ** 2)
                heappush(heap, (now_cost, i))

    return cost


for tc in range(1, int(input()) + 1):
    n = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    e = float(input())
    arr = []
    for i in range(n):
        arr.append((x_list[i], y_list[i]))
    ans = int(round(prim(0), 0))        # 소수점 첫째 자리에서 반올림 후 정수형으로 표현
    print(f'#{tc} {ans}')







